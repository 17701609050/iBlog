# -*- coding: utf-8 -*-
import uuid
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegisterForm
from apps.user.models import Profile
from ..utils.email import send_verify_email


def user_login(request):
    target_uri = request.POST.get('targetUri') or request.GET.get('targetUri', '')
    context = {}
    context.update({'targetUri': target_uri, 'error_msg': ''})
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)
                if target_uri:
                    return redirect(target_uri)
                return redirect("/blog/all/")
            else:
                context.update({'form': user_login_form, 'error_msg': '用户名或密码错误'})
                return render(request, 'common/login.html', context)
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context.update({'form': user_login_form})
        return render(request, 'common/login.html', context)


def user_sign_up(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        context = {'form': user_register_form}
        if user_register_form.is_valid():
            username = user_register_form.cleaned_data['username']
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password2']
            with transaction.atomic():
                new_user = User.objects.create_user(username=username, email=email, password=password)
                uid = ''.join(str(uuid.uuid4()).split('-'))
                Profile.objects.create(user=new_user, uid=uid)
            # 保存好数据后立即登录并返回博客列表页面
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            send_verify_email(user.email)
            return redirect("/user/profile/{}/".format(uid))
        else:
            context['error_msg'] = user_register_form.errors
            return render(request, 'common/sign_up.html', context)
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        return render(request, 'common/sign_up.html', {'form': user_register_form})
    else:
        return HttpResponse("请使用GET或POST请求数据")


# 用户退出
def user_logout(request):
    logout(request)
    return redirect("/user/login/")


def profile(request, uid):
    pro_file = Profile.objects.get(uid=uid)
    profile_tags = pro_file.tags.all()
    return render(request, 'common/profile.html', {'profile': pro_file, 'profile_tags': profile_tags})
