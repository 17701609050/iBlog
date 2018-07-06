# -*- coding: UTF-8 -*-
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.core.cache import cache
from .service import SessionArgs, SysPermUserService, SysRoleService, SysFunService, SysAuthService, SysMenuService, string2JSON
from .models import SysRPermissionUser, SysMRole, SysMFun, SysMMenu, SysMAuthority, DjLogSessionData

# if settings.SESSION_REDIS_PREFIX is not None:
#     CACHE_PREFIX = settings.SESSION_REDIS_PREFIX + ':'
# else:
#     CACHE_PREFIX = ''
#
# sysper_instance = SysPermUserService(SysRPermissionUser)
# sysrole_instance = SysRoleService(SysMRole)
# sysfun_instance = SysFunService(SysMFun)
# sysmenu_instance = SysMenuService(SysMMenu)
# syauth_instance = SysAuthService(SysMAuthority)
#
#
# def do_login(request, manual=None):
#     """
#     :param request: request object
#     :param manual: 是否自动登录
#     :return: 验证结果
#     """
#     user_authenticated = False
#     session_data = ''
#     username = request.REQUEST.get('username', '').strip()
#     password = request.REQUEST.get('password', '').strip()
#     manual = request.COOKIES.get(SessionArgs.STAFF_TOKEN) is None if manual is None else manual
#     # 手动登录，验证登录身份(同时验证用户名+密码).
#     if manual:
#         # 验证用户名+密码
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             user_authenticated = user.is_active
#             if user_authenticated:
#                 login(request, user)
#     else:  # IDSID 直接登录
#         # Authenticate from via Circuit
#         username = request.COOKIES.get(SessionArgs.STAFF_TOKEN, username)
#         if username:
#             try:
#                 user = User._default_manager.get_by_natural_key(username)
#             except User.DoesNotExist:
#                 user = User(username=username,
#                             password=password,
#                             is_superuser=0,
#                             is_active=1,
#                             is_staff=0,
#                             date_joined=get_utc_now(),
#                             last_login=get_utc_now(),
#                             first_name=username,
#                             last_name=username,
#                             email=username+'@intel.com')
#                 user.save()
#             user.backend = 'django_auth_ldap.backend.LDAPBackend'
#             login(request, user)
#             user_authenticated = True
#         else:
#             user_authenticated = False
#
#     # 认证通过
#     if user_authenticated:
#         session_data = build_sso(request)
#
#     return user_authenticated, session_data
#
# def build_sso(request):
#     user_role = build_user_role(request)
#     return build_user_session(request, user_role)
#
#
# def build_user_role(request):
#
#     # 如果在session里有用户role的权限(已登录)直接返回当前session_data
#     # 否则需要用户名重新去获取用户的role
#     if SessionArgs.AUTHOR_ROLES in request.session:
#         return request.session[SessionArgs.AUTHOR_ROLES]
#     else:
#         userRole = sysper_instance.getUserPermByName(request.user.username)
#         if userRole is None:
#             # allow anonymous access
#             user_role = SessionArgs.ANONYMOUS_ROLE
#         else:
#             user_role = userRole.user_role
#             # everyone is anonymous
#             user_role = user_role.strip(',') + ',' + SessionArgs.ANONYMOUS_ROLE
#
#         return user_role
#
# def build_user_session(request, user_role):
#     def build_session(req, cache_key, u_role):
#         user_role_code = []
#         user_role_menu_filter = {}
#         user_role_menu_list = []
#         for item in sysrole_instance.findRoleIDByCodes(u_role.split(',')):
#             user_role_code.append(item['role_code'])
#             # if item['remark'] and str(item['remark']).strip() != '':
#             #     role_menu_filter = string2JSON(item['remark'])
#             #     for menu_filter in role_menu_filter:
#             #         if menu_filter in user_role_menu_filter:
#             #             user_role_menu_filter[menu_filter] += "," + role_menu_filter[menu_filter]
#             #         else:
#             #             user_role_menu_filter[menu_filter] = role_menu_filter[menu_filter]
#         print user_role_code
#         menu_code_list = []
#         for rolecode in user_role_code:
#             menucode = syauth_instance.find_menu_code(rolecode)
#             menu_code_list += menucode
#         print list(set(menu_code_list))
#         menu_code_list = sorted(list(set(menu_code_list)))
#         menu_tree_list = sysmenu_instance.get_menu_node_tree_by_root(menu_code_list)
#         menu_html_string = sysmenu_instance.get_menus_html(menu_tree_list)
#         print menu_html_string
#         # user_auth_list = syauth_instance.findDinMenuFunByMutilRole(user_role_code)
#         # all_fun_list = {}  # all function dict
#         # sys_fun_list = []  # all menu list
#         # for fun_obj in sysfun_instance.find_list():
#         #     all_fun_list[fun_obj.fun_code] = fun_obj.__dict__
#         # for sysMenu in sysmenu_instance.find_list():
#         #     sys_menu_dict = sysMenu.__dict__  # system function list
#         #     sys_menu_dict['functions'] = []
#         #     if sysMenu.menu_code in user_auth_list:
#         #         if user_auth_list.get(sysMenu.menu_code):
#         #             for fun_code in user_auth_list[sysMenu.menu_code]:
#         #                 sys_menu_dict['functions'].append(all_fun_list.get(fun_code, ''))
#         #         sys_fun_list.append(sys_menu_dict)
#
#         # get tree node
#         # is_rest_request = bool(req.META.get('X_USER_ORIGIN') and req.META['X_USER_ORIGIN'])
#         # if not is_rest_request: #@bug: REST USER is no separate authority
#         # menu_tree = SysMMenu.get_menu_node_tree_by_root()
#         # menu_html_string = get_menus_string_from_session(req, menu_tree, user_auth_list)
#         # menu_html_string = SysMMenu.get_validation_report_menu_style_string(req, user_auth_list, menu_html_string)
#
#         # save into redis
#         return {
#                 SessionArgs.SYS_MENU_HTML: menu_html_string,
#                 # SessionArgs.SYS_MENU_LIST: menu_html_string,
#                 SessionArgs.AUTHOR_ROLES: user_role,
#                 SessionArgs.USER_TOKEN: cache_key,
#                 SessionArgs.ENCRYPT_STRING: request.session.session_key,
#                 SessionArgs.USER_ROLE_MENU_FILTER: user_role_menu_filter
#         }
#
#     role_cache_key = CACHE_PREFIX # + sysCategoryService.saveOrUpdateCategory(SessionArgs.CATEGORY_OWNER, user_role)
#     _session_data = build_session(request, role_cache_key, user_role)
#
#     if settings.SESSION_ENGINE_ALIAS == 'redis':
#         session_data = cache.get(role_cache_key)
#         if session_data is None:
#             cache.set(role_cache_key, _session_data, timeout=settings.SESSION_CACHE_TIMEOUT)
#     else:
#         session_data = DjLogSessionData.objects.filter(session_key=role_cache_key).first()
#         if session_data is None:
#             session_data = DjLogSessionData()
#             session_data.session_key = role_cache_key
#             session_data.session_data = _session_data
#             session_data.set_encode_data()
#             session_data.save()
#
#     # save to session
#     request.session[SessionArgs.AUTHOR_ROLES] = _session_data[SessionArgs.AUTHOR_ROLES]
#     request.session[SessionArgs.USER_TOKEN] = _session_data[SessionArgs.USER_TOKEN]
#     request.session.modified = True  # flush session
#
#     return _session_data
#
# def get_utc_now(str_format=False):
#     if str_format:
#         return timezone.now().strftime("%Y-%m-%d %H:%M:%S")
#     else:
#         return timezone.now()