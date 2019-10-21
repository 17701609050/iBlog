# -*- coding: utf-8 -*-
import requests
import json
import time
import uuid
import urllib, urllib.request
from urllib.parse import urlparse
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from apps.user.models import Profile


class OAuthQQ:
    def __init__(self, client_id, client_key, redirect_uri):
        self.client_id = client_id
        self.client_key = client_key
        self.redirect_uri = redirect_uri

    def get_auth_url(self):
        """获取授权页面的网址"""
        params = {'client_id': self.client_id,
                  'response_type': 'code',
                  'redirect_uri': self.redirect_uri,
                  'scope': 'get_user_info',
                  'state': 1}
        url = 'https://graph.qq.com/oauth2.0/authorize?%s' % urllib.urlencode(params)
        return url

    def get_access_token(self, code):
        """根据code获取access_token"""
        params = {'grant_type': 'authorization_code',
                  'client_id': self.client_id,
                  'client_secret': self.client_key,
                  'code': code,
                  'redirect_uri': self.redirect_uri}  # 回调地址
        url = 'https://graph.qq.com/oauth2.0/token?%s' % urllib.urlencode(params)

        # 访问该网址，获取access_token
        response = urllib.request.urlopen(url).read()
        result = urlparse.parse_qs(response, True)

        access_token = str(result['access_token'][0])
        self.access_token = access_token
        return access_token

    def get_open_id(self):
        """获取QQ的OpenID"""
        params = {'access_token': self.access_token}
        url = 'https://graph.qq.com/oauth2.0/me?%s' % urllib.urlencode(params)

        response = urllib.request.urlopen(url).read()
        v_str = str(response)[9:-3]  # 去掉callback的字符
        v_json = json.loads(v_str)

        openid = v_json['openid']
        self.openid = openid
        return openid

    def get_qq_info(self):
        """获取QQ用户的资料信息"""
        params = {'access_token': self.access_token,
                  'oauth_consumer_key': self.client_id,
                  'openid': self.openid}
        url = 'https://graph.qq.com/user/get_user_info?%s' % urllib.urlencode(params)

        response = urllib.request.urlopen(url).read()
        return json.loads(response)


def qq_login(request, targetUri):
    oauth_qq = OAuthQQ(settings.QQ_APP_ID, settings.QQ_KEY, settings.QQ_RECALL_URL)

    # 获取 得到Authorization Code的地址
    url = oauth_qq.get_auth_url()
    # 重定向到授权页面
    request.session['targetUri'] = targetUri
    return HttpResponseRedirect(url)


def qq_auth(request):  # 第三方QQ登录，回调函数
    """登录之后，会跳转到这里。需要判断code和state"""
    request_code = request.GET.get('code')
    targetUri = request.session['targetUri']
    oauth_qq = OAuthQQ(settings.QQ_APP_ID, settings.QQ_KEY, settings.QQ_RECALL_URL)

    # 获取access_token
    access_token = oauth_qq.get_access_token(request_code)
    time.sleep(0.05)  # 稍微休息一下，避免发送urlopen的10060错误
    open_id = oauth_qq.get_open_id()
    # print open_id
    infos = oauth_qq.get_qq_info()
    # print infos
    username = infos['nickname']
    profile_image_url = infos.get('figureurl_qq', '')
    password = '111111'
    try:
        user1 = User.objects.get(username=username)
    except:
        user2 = User.objects.create_user(username=username, password=password)
        uid = ''.join(str(uuid.uuid4()).split('-'))
        Profile.objects.create(user_image=profile_image_url, user_from='qq', user=user2, uid=uid)

        # 登陆认证
    user = authenticate(username=username, password=password)
    login(request, user)
    if targetUri:
        return redirect(targetUri)
    return HttpResponseRedirect(reverse('index'))
    # 检查open_id是否存在
    # qq_open_id = models.OAuthQQ.objects.filter(qq_openid=str(open_id))
    # print qq_open_id
    # if qq_open_id:
    #     # 存在则获取对应的用户，并登录
    #     user = qq_open_id[0].user.username
    #     print user
    #     request.session['username'] = user
    #     return HttpResponseRedirect('/web/')
    # else:
    #     # 不存在，则跳转到绑定用户页面
    #     infos = oauth_qq.get_qq_info()  # 获取用户信息
    #     url = '%s?open_id=%s&nickname=%s' % (reverse('bind_account'), open_id, infos['nickname'])
    #     return HttpResponseRedirect(url)
