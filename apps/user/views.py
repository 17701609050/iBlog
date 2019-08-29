# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegisterForm
from apps.user.models import Profile
from ..utils.email import send_verify_email


def user_login(request):
    target_uri = request.POST.get('targetUri') or request.GET.get('targetUri')
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
                return redirect("/profile/")
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        if target_uri:
            context.update({'targetUri': target_uri})
        return render(request, 'common/login.html', context)


def user_sign_up(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # 设置密码
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # 保存好数据后立即登录并返回博客列表页面
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            # send_verify_email(user.email, 'http://zipinglx.sh.intel.com:8081')
            return redirect("/profile/")
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = {'form': user_register_form}
        return render(request, 'common/sign_up.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


# 用户退出
def user_logout(request):
    logout(request)
    return redirect("/user/login/")


def profile(request):
    pro_file = Profile.objects.get(user=request.user)
    profile_tags = pro_file.tags.all()
    return render(request, 'common/profile.html', {'profile': pro_file, 'profile_tags': profile_tags})
