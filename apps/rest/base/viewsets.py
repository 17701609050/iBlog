# -*- coding: utf-8 -*-
import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

from rest_framework_swagger.views import get_swagger_view

from django.conf.urls import url, include

# from icgfuture.configuration import config
# from apps.dashboard.services import SysMenuService
# from apps.dashboard.sso import do_login
# from apps.validation.models import *
# from apps.api.utils import SessionArgs, injection_data_to_req, get_guid_list_bettwen_two_iso_date
# from apps.rest.base.auth import platform_permission_control
from .serializers import *


# router = DefaultRouter()

"""
    System api for view set
    ViewSets define the view behavior.
"""


# class PlatformView(viewsets.GenericViewSet):
#     """
#     Returns a list of all **active** accounts in the system platform.
#
#     [ref]: http://${domain}/rest/docs/#!/platform/platform_get_allowed_read
#     """
#     def get_queryset(self):
#         return self.get_serializer_class().Meta.model.objects.filter(is_allowed=Platform.Status.ALLOWED)
#
#     def get_serializer_class(self):
#         return PlatformSerializer
#
#     @list_route(methods=['GET'])
#     def get_allowed(self, request, *args, **kwargs):
#
#         if request.data:
#             platform_name = request.data.get('platform')
#         else:
#             platform_name = request.query_params.get('platform_name')
#
#         recent_platform = self.get_queryset().order_by('platform_name')
#         if platform_name:
#             recent_platform = recent_platform.filter(platform_name=platform_name).first()
#             kwargs['many'] = False
#         else:
#             kwargs['many'] = True
#
#         if recent_platform:
#             serializer = self.get_serializer(recent_platform, **kwargs)
#             recent_platform = serializer.data
#             recent_platform = platform_permission_control(request, recent_platform)
#
#         return Response(data=recent_platform, status=status.HTTP_200_OK)
#
#     @list_route(methods=['GET'])
#     def get_allowed_without_authentication(self, request, *args, **kwargs):
#         if request.data:
#             platform_name = request.data.get('platform')
#         else:
#             platform_name = request.query_params.get('platform_name')
#
#         recent_platform = self.get_queryset().order_by('platform_name')
#         if platform_name:
#             recent_platform = recent_platform.filter(platform_name=platform_name).first()
#             kwargs['many'] = False
#         else:
#             kwargs['many'] = True
#
#         if recent_platform:
#             serializer = self.get_serializer(recent_platform, **kwargs)
#             recent_platform = serializer.data
#
#         return Response(data=recent_platform, status=status.HTTP_200_OK)
#
#     @list_route(methods=['POST'])
#     def get_between_two_time_guid_data(self, request, *args, **kwargs):
#         guid_list = get_guid_list_bettwen_two_iso_date(request.data['start_time'], request.data['end_time'])
#         type = int(request.data['type'])
#         if request.data.get('platform'):
#             sub_platform_dict_list = []
#             for guid in guid_list:
#                 sub_platform_dict_list.extend(TestGuid.objects.filter(year=guid['year'], ww=guid['ww'], day=guid['day']
#                                                                   , type=type, platform=request.data['platform']).values('sub_platform'))
#             _list = list(set([i['sub_platform'] for i in sub_platform_dict_list]))
#         else:
#             platform_dict_list = []
#             for guid in guid_list:
#                 platform_dict_list.extend(TestGuid.objects.filter(year=guid['year'], ww=guid['ww'], day=guid['day']
#                                                   , type=type).values('platform', 'sub_platform'))
#             _list = list(set([i['platform'] for i in platform_dict_list]))
#         return Response(data=_list, status=status.HTTP_200_OK)
#
#     @list_route(methods=['POST'])
#     def get_between_two_time_sub_platform_from_request(self, request, *args, **kwargs):
#         guid_list = get_guid_list_bettwen_two_iso_date(request.data['start_time'], request.data['end_time'])
#         type = int(request.data['type'])
#         sub_platform_dict_list = []
#         if request.data.get('platform'):
#             for guid in guid_list:
#                 sub_platform_dict_list.extend(TestGuid.objects.filter(year=guid['year'], ww=guid['ww'], day=guid['day']
#                                                                   , type=type, platform=request.data['platform']).values('sub_platform'))
#         else:
#             for guid in guid_list:
#                 sub_platform_dict_list.extend(TestGuid.objects.filter(year=guid['year'], ww=guid['ww'], day=guid['day']
#                                                                   , type=type).values('sub_platform'))
#         _list = list(set([i['sub_platform'] for i in sub_platform_dict_list]))
#         return Response(data=_list, status=status.HTTP_200_OK)
#
#     @list_route(methods=['POST'])
#     def test_case_query(self, request, *args, **kwargs):
#         guid_list = get_guid_list_bettwen_two_iso_date(request.data['start_time'], request.data['end_time'])
#         type = int(request.data['type'])
#         TYPE_MODEL_MAP = {
#             1: WeeklyTestDetail,
#             2: PITDetail,
#             3: PITLiteDetail,
#             4: CITDetail
#         }
#         viewset_model = TYPE_MODEL_MAP[type]
#         test_case_id_list = []
#         for guid in guid_list:
#             guid.update({'type': type})
#             if request.data.get('platform'):
#                 guid.update({'platform': request.data['platform']})
#             if request.data.get('sub_platform'):
#                 guid.update({'sub_platform': request.data['sub_platform']})
#             for test_guid in TestGuid.objects.filter(**guid):
#                 test_case_id_list.extend(
#                     viewset_model.objects.filter(guid=test_guid).values('case_id'))
#         test_case_id_list = list(set([i['case_id'] for i in test_case_id_list]))
#         return Response(data=test_case_id_list, status=status.HTTP_200_OK)
#
# router.register(r'platform', PlatformView, 'platform')


# class ProjectView(viewsets.ModelViewSet):
#
#     def get_queryset(self):
#         return self.get_serializer_class().Meta.model.objects.filter(data_status=Project.DATA_EFFECT)
#
#     def get_serializer_class(self):
#         return ProjectSerializer
#
#     @list_route(methods=['GET'])
#     def get_list(self, request, *args, **kwargs):
#
#         all_project = self.get_queryset().order_by('project_name')
#         serializer = self.get_serializer(all_project, many=True)
#
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
# router.register(r'project', ProjectView, 'project')


# class SysMenuView(mixins.CreateModelMixin,
#                   mixins.DestroyModelMixin,
#                   viewsets.GenericViewSet):
#
#     def create(self, request, *args, **kwargs):
#         # get args from post data
#         report_type = request.data.get('report_type', request.data.get('type'))
#         if isinstance(report_type, int) or report_type.isdigit():
#             report_type = TestGuid(type=int(report_type)).get_type_display()
#         platform = request.data.get('platform')
#         sub_platform = request.data.get('sub_platform')
#
#         # 1: save or update menu
#         sysMenuService = SysMenuService()
#         # mounts point name  'report' in settings
#         mount_menu = sysMenuService.get_menu_mount_points(report_type)
#         if mount_menu:
#             # 2 split platform name
#             plats = platform.split('-')
#             if len(plats) == 1:
#                 parent_menu_code = sysMenuService.save_or_create_menu(request, mount_menu.menu_code, platform,
#                                                                       '#', tag=report_type)
#             else:
#                 # insert SDK menu node
#                 parent_menu_code = sysMenuService.save_or_create_menu(request, mount_menu.menu_code, plats[0],
#                                                                       '#', tag=report_type)
#
#                 # insert os menu node
#                 parent_menu_code = sysMenuService.save_or_create_menu(request, parent_menu_code, plats[2],
#                                                                       '#', tag=report_type)
#                 # insert platform menu node
#                 parent_menu_code = sysMenuService.save_or_create_menu(request, parent_menu_code, plats[1],
#                                                                       '#', tag=report_type)
#
#             # insert sub platform node
#             sysMenuService.save_or_create_menu(request, parent_menu_code, sub_platform,
#                                                sysMenuService.assembled_url(
#                                                    '/'.join((config('AUTO_MENU_PREFIX'), report_type,)),
#                                                    {'platform': platform, 'sub_platform': sub_platform}), is_last=True)
#
#         return Response(status=status.HTTP_201_CREATED)
#
#     def create_invisible(self, request, *args, **kwargs):
#         # get args from post data
#         report_type = request.data.get('report_type', request.data.get('type'))
#         if isinstance(report_type, int) or report_type.isdigit():
#             report_type = TestGuid(type=int(report_type)).get_type_display()
#         platform = request.data.get('platform')
#         sub_platform = request.data.get('sub_platform')
#
#         # 1: save or update menu
#         sysMenuService = SysMenuService()
#         mount_menu = sysMenuService.get_menu_mount_points(report_type)
#         if mount_menu:
#             # 2 split platform name
#             plats = platform.split('-')
#             if len(plats) == 1:
#                 parent_menu_code = sysMenuService.save_or_create_menu(request, mount_menu.menu_code, platform, '#')
#             else:
#                 # insert SDK menu node
#                 parent_menu_code = sysMenuService.save_or_create_menu(request, mount_menu.menu_code, plats[0], '#')
#                 # insert os menu node
#                 parent_menu_code = sysMenuService.save_or_create_menu(request, parent_menu_code, plats[2], '#')
#                 # insert platform menu node
#                 parent_menu_code = sysMenuService.save_or_create_menu(request, parent_menu_code, plats[1], '#')
#
#             # insert sub platform node
#             sysMenuService.save_or_create_menu(request, parent_menu_code, sub_platform,
#                                                sysMenuService.assembled_url(
#                                                    '/'.join((config('AUTO_MENU_PREFIX'), report_type,)),
#                                                    {'platform': platform, 'sub_platform': sub_platform}), visible=0, is_last=True)
#
#         return Response(status=status.HTTP_201_CREATED)
#
#     def destroy(self, request, *args, **kwargs):
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def login(request):
#
#     # set rest request flag
#     request.META['X_USER_ORIGIN'] = SessionArgs.X_USER_ORIGIN
#     dict_params = request.data or request.query_params
#     # execute login
#     user_name = dict_params.get('username')
#     user_pwd = dict_params.get('password')
#     if user_name is None or user_pwd is None:
#         return Response(data={'message': 'user name and password can not be null.'}, status=status.HTTP_400_BAD_REQUEST)
#
#     # Initialize session
#     injection_data_to_req(request._request, "user_name", user_name)
#     injection_data_to_req(request._request, "user_pwd", user_pwd)
#     (user_authenticated, session_data,) = do_login(request._request,  manual=True)
#
#     if not user_authenticated:
#         return Response(data={'message': 'authentication failed，initialize session fail.'},
#                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     else:
#         from django.middleware import csrf
#         return Response(data={'csrfmiddlewaretoken': csrf.get_token(request)}, status=status.HTTP_200_OK)
#
#
# schema_view = get_swagger_view(title='Rest API Docs & Test')
# urls = [
#     url(r'^docs/$', schema_view),
#     url(r'', include(router.urls)),
#     url(r'^login/', login, name='rest_login'),
# ]
