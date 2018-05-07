# -*- coding: utf-8 -*-
"""
@Created on 2016-04-15
@Author: gaobo.xiao
@Version V1.0
"""
import re
import json
import logging
import traceback

from django.contrib import auth
from django.http import HttpResponse
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.permissions import BasePermission
# from apps.api.utils import SessionArgs


def login_filter():
    """ API caller login filter
        :return: 1) Not logged directly rejected
                 2) Logged user permissions to inject in data
    """
    def _login_filter(func):
        def __login_filter(request, **data):
            """
                :param request>>user_info: API caller user info:{username: xxxx, password: ****}
            """
            # init caller right
            data.update({'write': False, 'read': False})
            # init return message
            return_msg = {'status': '-1', 'message': '', 'data': {}}
            try:
                name = request.REQUEST['username']
                pwd = request.REQUEST['password']
            except KeyError, e:
                print ('Please input username and password: %s' % str(e))
                comment = 'Please input username and password!'
                return_msg['message'] = comment
                return HttpResponse(json.dumps(return_msg), status=200)

            if name and pwd:
                user = auth.authenticate(username=name.lower(), password=pwd)
                if user is not None and user.is_active:
                    try:
                        str_attrs = str(user.ldap_user.attrs)
                        dict_attrs = dict(eval(str_attrs))
                        memberof = dict_attrs.get('memberof')  # Get the user group information.
                        usr_groups = list()

                        for group in memberof:
                            group_name = group.split(',')[0].split('=')[1]
                            usr_groups.append(group_name)

                        if 'ICG_Dashboard_Write' in usr_groups:
                            data['write'] = True

                        if 'ICG_Dashboard_Read_Only' in usr_groups:
                            data['read'] = True

                    except Exception, e:
                        print(str(e))

                elif user is not None and not user.is_active:
                    comment = 'You are not authorized !'
                    return_msg['message'] = comment
                    return HttpResponse(json.dumps(return_msg), status=200)
                else:
                    comment = 'Invalid username or password !'
                    print(comment)
                    return_msg['message'] = comment
                    return HttpResponse(json.dumps(return_msg), status=200)
            else:
                comment = 'User your Windows IDSID and Password to login !'
                print(comment)
                return_msg['message'] = comment
                return HttpResponse(json.dumps(return_msg), status=200)

            return func(request, data)

        return __login_filter
    return _login_filter


def do_process_decorator(process_decorate):
    """
    :param process_decorate:
    :return:
    """
    def wrapper(request, report_type, data):
        try:
            if not request.REQUEST.get('report_data'):
                return_msg = {'status': '-1', 'message': 'parameter error', 'data': {}}
                return HttpResponse(json.dumps(return_msg), status=200)
            else:
                data['msg'] = {'status': '2', 'message': [], 'data': {}}
                return process_decorate(request, report_type, data)
            # caller no write permission
            if not data.get('write'):
                return_msg = {'status': '-1', 'message': 'User is not authorized to make change on DB', 'data': {}}
                return HttpResponse(json.dumps(return_msg), status=200)

        except KeyError as keyErr:
            data['msg'] = {'status': '-1', 'message': 'Invalid format REPORT TYPE: %s Detail: %s' %
                                                      ('None' if report_type == 'all' else report_type, str(keyErr)),'data': {}}
            return HttpResponse(content=json.dumps(data['msg']), status=204)
        except Exception as e:
            logging.getLogger('django').error(traceback.format_exc())
            return_msg = {'status': '-1', 'message': str(e), 'data': {}}
            return HttpResponse(content=json.dumps(return_msg), status=500)
    return wrapper

# def platform_permission_control(request, data):
#     """
#     Platform permission deny by session USER_ROLE_MENU_FILTER
#     """
#     if data:
#         if 'admin' in request.session_data.get(SessionArgs.AUTHOR_ROLES, ''):
#             return data
#         user_role_filter = request.session_data.get(SessionArgs.USER_ROLE_MENU_FILTER, {})
#         res = []
#         if user_role_filter:
#             for r in user_role_filter:
#                 pattern = re.compile(r, re.IGNORECASE)
#                 data = [data] if isinstance(data, dict) else data
#                 for i in data:
#                     match = pattern.match(i['platform_name'])
#                     if match:
#                         res.append(i)
#             return res
#         else:
#             return []
#     else:
#         return []

# class ICGAuthentication(BaseAuthentication):
#
#     def authenticate(self, request):
#         # username = request.META.get('HTTP_USERNAME')
#         # # print username, request.META.get('HTTP_PASSWORD')
#         # if not username:
#         #     return None
#         # # LOGIN
#         # # return user, auth
#         # return username, None,
#         pass
#
#
#     def check_permission(self, request):
#         #admin skip the check
#         if 'admin' in request.session_data.get(SessionArgs.AUTHOR_ROLES, ''):
#             return False
#         data = request.data['guid'] if request.data.get('guid') else request.data
#         #mq send user role filter
#         if data.get('user_role_filter', '') or data.get('user_role_filter', '') == {}:
#             user_role_filter = data.get('user_role_filter')
#         else:
#             user_role_filter = request.session_data.get(SessionArgs.USER_ROLE_MENU_FILTER, {})
#         #pit summary has not have platform in guid
#         if 'platform' not in data.keys():
#             return False
#         if user_role_filter:
#             for r in user_role_filter:
#                 pattern = re.compile(r, re.IGNORECASE)
#                 match = pattern.match(data.get('platform', ''))
#                 if match:
#                     break
#             else:
#                 return True
#         else:
#             return True
#         return False

class ICGAPIAuthentication(BaseAuthentication):

    def __init__(self, param):
        self.param = param

    def authenticate(self, request):
        value_list = []
        for ii in request.REQUEST:
            if ii:
                for i in ii.keys():
                    value_list.append(i)
        for _i in self.param:
            if _i not in value_list:
                return_msg = {'status': '-1', 'message': 'Missing parameter %s' % _i}
                return HttpResponse(json.dumps(return_msg), status=200)


class ICGRestPermission(BasePermission):

    def has_permission(self, request, view):
        print view
        return False

    def has_read_permission(self, request):
        return True

    def has_object_read_permission(self, request):
        return True

    def has_write_permission(self, request):
        return False

    def has_create_permission(self, request):
        return True

