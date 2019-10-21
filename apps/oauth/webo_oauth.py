# -*- coding: utf-8 -*-
import requests
import json
import time
import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from apps.user.models import Profile


class OAuthWB:
    def __init__(self, client_id, client_key, redirect_uri):
        self.client_id = client_id
        self.client_key = client_key
        self.redirect_uri = redirect_uri

    def get_access_token(self, code):  # 获取用户token和uid
        url = "https://api.weibo.com/oauth2/access_token"

        querystring = {
            "client_id": self.client_id,
            "client_secret": self.client_key,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri
        }

        response = requests.request("POST", url, params=querystring)

        return json.loads(response.text)

    def get_user_info(self, access_token_data):
        url = "https://api.weibo.com/2/users/show.json"

        querystring = {
            "uid": access_token_data['uid'],
            "access_token": access_token_data['access_token']
        }

        response = requests.request("GET", url, params=querystring)

        return json.loads(response.text)


def weibo_login(request, targetUri):   # 跳转授权页面
    request.session['targetUri'] = targetUri
    return HttpResponseRedirect(
        'https://api.weibo.com/oauth2/authorize?client_id={0}&redirect_uri={1}'.format(
            settings.WEIBO_APP_ID,
            settings.WEIBO_CALLBACK
            )
    )


def webo_auth(request):
    """登录之后，会跳转到这里。需要判断code和state"""
    code = request.GET.get('code', None)
    targetUri = request.session['targetUri']
    sina = OAuthWB(settings.WEIBO_APP_ID, settings.WEIBO_APP_KEY, settings.WEIBO_CALLBACK)
    user_info = sina.get_access_token(code)
    time.sleep(0.1)  # 防止还没请求到token就进行下一步
    # 通过uid查询出是否是新用户，新用户则注册登录
    # 如果不存在username，则创建
    new_user_info = sina.get_user_info(user_info)
    # print new_user_info
    username = new_user_info['name']
    profile_image_url = new_user_info.get('avatar_large', '')
    password = '111111'
    try:
        user1 = User.objects.get(username=username)
    except:
        user2 = User.objects.create_user(username=username, password=password)
        uid = ''.join(str(uuid.uuid4()).split('-'))
        Profile.objects.create(user_image=profile_image_url, user_from='weibo', user=user2, uid=uid)

    # 登陆认证
    user = authenticate(username=username, password=password)
    login(request, user)
    if targetUri:
        return redirect(targetUri)
    return HttpResponseRedirect(reverse('index'))
