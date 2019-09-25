# -*- coding: UTF-8 -*-
import urllib
import urllib2
import json
import uuid
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from apps.user.models import Profile


GITHUB_CLIENTID = settings.GITHUB_CLIENTID
GITHUB_CLIENTSECRET = settings.GITHUB_CLIENTSECRET
GITHUB_CALLBACK = settings.GITHUB_CALLBACK
GITHUB_AUTHORIZE_URL = settings.GITHUB_AUTHORIZE_URL


def _get_refer_url(request):
    refer_url = request.META.get('HTTP_REFER', '/index/')
    host = request.META['HTTP_HOST']
    if refer_url.startswith('http') and host not in refer_url:
        refer_url = '/'
    return refer_url


# 第一步: 请求github第三方登录
def githhub_login(request, targetUri):
    data = {
        'client_id': GITHUB_CLIENTID,
        'client_secret': GITHUB_CLIENTSECRET,
        'redirect_uri': GITHUB_CALLBACK+'?targetUri={}'.format(targetUri),
        'state': _get_refer_url(request),
    }

    print urllib.urlencode(data)
    github_auth_url = '%s?%s' % (GITHUB_AUTHORIZE_URL, urllib.urlencode(data))
    return HttpResponseRedirect(github_auth_url)


# github认证处理
def github_auth(request):
    template_html = 'common/login.html'

    # 如果申请登陆页面成功后，就会返回code和state(被坑了好久)
    if 'code' not in request.GET:
        return render(request, template_html)

    code = request.GET.get('code')
    targetUri = request.GET.get('targetUri')

    # 第二步
    # 将得到的code，通过下面的url请求得到access_token
    url = 'https://github.com/login/oauth/access_token'
    data = {
        'grant_type': 'authorization_code',
        'client_id': GITHUB_CLIENTID,
        'client_secret': GITHUB_CLIENTSECRET,
        'code': code,
        'redirect_uri': GITHUB_CALLBACK,
    }

    data = urllib.urlencode(data)

    # 请求参数需要bytes类型
    binary_data = data.encode('utf-8')

    # 设置请求返回的数据类型
    headers = {'Accept': 'application/json'}
    req = urllib2.Request(url, binary_data, headers)#urllib.request.Request(url, binary_data, headers)

    response = urllib2.urlopen(req)
    response_data = response.read()

    result = json.loads(response_data)
    access_token = result['access_token']

    url = 'https://api.github.com/user?access_token=%s' % (access_token)
    req = urllib2.Request(url)  #
    response = urllib2.urlopen(req)
    html = response.read()
    data = json.loads(html)
    username = data['name']
    # print('username:', username)
    password = '111111'
    profile_image_url = data.get('avatar_url', '')
    # 如果不存在username，则创建
    try:
        user = User.objects.get(username=username)
    except:
        user2 = User.objects.create_user(username=username, password=password)
        uid = ''.join(str(uuid.uuid4()).split('-'))
        Profile.objects.create(user_image=profile_image_url, user_from='github', user=user2, uid=uid)

    # 登陆认证
    user = authenticate(username=username, password=password)
    login(request, user)
    if targetUri:
        return redirect(targetUri)
    return HttpResponseRedirect(reverse('index'))
