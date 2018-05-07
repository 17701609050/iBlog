# -*- coding: utf-8 -*-
"""
@Created serializers.py on 16-5-5 PM 12:00
@Author: Gaobo.Xiao
@Version: V0.1
@license: Intel-ICG
@description: Serializers define the API representation.
"""
import sys
from functools import wraps

from rest_framework import serializers

# from apps.dashboard.models import Platform, Project, Version, Attachment
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

# from apps.api.mail import send_exception_email

def serializer_arg_assembly():
    def _serializer_arg_assembly(func):
        @wraps(func)
        def __serializer_arg_assembly(self, *args, **kwargs):
            if kwargs.get('context') and kwargs['context'].get('request'):
                query_params = kwargs['context']['request'].data or kwargs['context']['request'].query_params
                query_fields = query_params.get('query_fields', None)
                if query_fields:
                    query_fields = query_fields.split(',')
                    for field_name in self.fields:
                        if field_name not in query_fields:
                            self.fields.pop(field_name)
            return func(self, *args, **kwargs)
        return __serializer_arg_assembly

    return _serializer_arg_assembly


# class ICGException(Exception):
#     """
#     REST Standard Exception Definition
#     """
#     exception_list = {
#         'ICG000001': 'Missing key parameters',
#         'ICG000002': 'Parameter is invalid or error',
#         'ICG100001': 'The guid is empty or the format is incorrect',
#         'ICG100002': 'This report was locked by dashboard',
#         'ICG100003': 'Invalid platform',
#         'ICG100004': 'Invalid data',
#         'ICG100005': 'Data check false',
#         'ICG100006': 'Permission denied',
#         'ICG100010': 'Value is invalid',
#     }
#
#     admin_mail_list = []
#
#     class LogInfo:
#         Warning = 0
#         Exception = 1
#
#     def __init__(self, error_code, error_text, log_info=0, mail=False):
#         message = '[%s: %s] %s' % (error_code, self.exception_list.get(error_code, 'unknown exception'), error_text)
#
#         # Call the base class constructor with the parameters it needs
#         super(ICGException, self).__init__(message)
#
#         self.error_detail = message
#         self.log_info = log_info
#
#         if mail:
#             self.get_cur_info()
#             send_exception_email(self.admin_mail_list, self.error_detail, self.log_info, self.file_name,
#                                  self.func_name, self.line_num)

    # def get_cur_info(self):
    #     self.func_name = sys._getframe().f_back.f_back.f_code.co_name #get current function name
    #     self.file_name = sys._getframe().f_back.f_back.f_code.co_filename# get current file name
    #     self.line_num = sys._getframe().f_back.f_back.f_lineno# get current file code number


class RequestDone(Exception):
    """
    Marker exception that stated any request processing has completed and a response was sent.
    """

    def __init__(self, *args, **kwargs):
        super(RequestDone, self, *args, **kwargs).__init__("request processing has completed")


# class VersionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Version
#         fields = '__all__'


# class PlatformSerializer(serializers.ModelSerializer):
#
#     @serializer_arg_assembly()
#     def __init__(self, *args, **kwargs):
#         super(PlatformSerializer, self).__init__(*args, **kwargs)
#
#     class Meta:
#         model = Platform
#         fields = ('id', 'platform_name', 'platform_desc', 'owned_os', 'is_standard')


# class ProjectSerializer(serializers.ModelSerializer):
#
#     @serializer_arg_assembly()
#     def __init__(self, *args, **kwargs):
#         super(ProjectSerializer, self).__init__(*args, **kwargs)
#
#     def create(self, validated_data):
#         return Project(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('project_name', instance.project_name)
#         return instance
#
#     class Meta:
#         model = Project
#         fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# class VersionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Version
#         fields = ('id', 'version_id', 'version_name', 'version_desc', 'version_type', 'is_active')


# class AttachmentSerializer(serializers.ModelSerializer):
#     filename = serializers.FileField(allow_empty_file=False, use_url=True)
#     type = serializers.ChoiceField(allow_blank=False, choices=Attachment.ATTACHMENT_TYPE_CHOICES, style={'base_template': 'radio.html'})
#     size = serializers.FloatField(allow_null=False)
#     time = serializers.DateTimeField(read_only=True)
#     description = serializers.CharField(allow_blank=True, allow_null=True)
#     author = serializers.CharField(max_length=45, allow_blank=True, allow_null=True)
#     ipnr = serializers.IPAddressField(max_length=255, allow_blank=True, allow_null=True)
#
#     def create(self, validated_data):
#         file_obj = validated_data['filename']
#         file_path = 'static/USER_UPLOADS/wiki/' + validated_data['filename'].name
#         with default_storage.open(file_path, 'wb+') as destination:
#             for chunk in file_obj.chunks():
#                 destination.write(chunk)
#         validated_data['filename'] = file_path
#         return Attachment(**validated_data)
#
#     class Meta:
#         # customize validators
#         validators = ()
#         model = Attachment
#         fields = '__all__'
