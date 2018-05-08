# -*- coding: UTF-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone

class SessionArgs(object):
    ENCRYPT_KEY = 119  # encrypt number key
    ENCRYPT_STRING = '***_icg_***'  # encrypt string
    USER_TOKEN = 'sessionid'  # user cookie key
    STAFF_TOKEN = 'IDSID'  # staff idsid cookie key
    UNAME_KEY = 'u_name'  # login name
    AUTHOR_ROLES = "author_role"  # login user author list
    SYS_MENU_HTML = 'sys_menu_html'  # login user menu string
    SYS_FUN_LIST = 'sys_fun_list'  # login user function string
    SYS_USER_CONFIG = 'sys_user_config'  # login user customize configuration
    USER_ROLE_MENU_FILTER = 'user_role_menu_filter'  # filter the menu's regular expression
    X_USER_ORIGIN = 'ICG_REST_API'
    # admin list
    SUPPER_ADMIN = 'icgadmin'
    ADMIN_LIST = ('icgadmin', 'admin',)
    ANONYMOUS_ROLE = 'anonymous'
    CATEGORY_OWNER = 'session_map'
    USER_BLACKLIST_PREFIX = 'USER_BLACKLIST:'

def do_login(request, manual=None):
    """
    :param request: request object
    :param manual: 是否自动登录
    :return: 验证结果
    """
    user_authenticated = False
    session_data = ''
    username = request.REQUEST.get('user_name', '').strip()
    password = request.REQUEST.get('user_pwd', '').strip()
    manual = request.COOKIES.get(SessionArgs.STAFF_TOKEN) is None if manual is None else manual
    # 手动登录，验证登录身份(同时验证用户名+密码).
    if manual:
        # 验证用户名+密码
        user = authenticate(username=username, password=password)
        if user is not None:
            user_authenticated = user.is_active
            if user_authenticated:
                login(request, user)
    else:  # 自动登录
        # Authenticate from via Circuit
        username = request.COOKIES.get(SessionArgs.STAFF_TOKEN, username)
        if username:
            try:
                user = User._default_manager.get_by_natural_key(username)
            except User.DoesNotExist:
                user = User(username=username,
                            password=password,
                            is_superuser=0,
                            is_active=1,
                            is_staff=0,
                            date_joined=get_utc_now(),
                            last_login=get_utc_now(),
                            first_name=username,
                            last_name=username,
                            email=username+'@intel.com')
                user.save()
            user.backend = 'django_auth_ldap.backend.LDAPBackend'
            login(request, user)
            user_authenticated = True
        else:
            user_authenticated = False

    # 认证通过
    if user_authenticated:
        session_data = build_sso(request)

    return user_authenticated, session_data

def get_utc_now(str_format=False):
    if str_format:
        return timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        return timezone.now()