# -*- coding: utf-8 -*-

import json
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import list_route
from rest_framework.generics import get_object_or_404
from django.shortcuts import get_list_or_404
# from apps.validation.models import TestGuid
from django.forms.models import model_to_dict


def get_view_invoke_data(cls, meth, request, *args, **kwargs):

    obj = cls()
    obj.request = request
    obj.format_kwarg = None
    if 'query_params' in kwargs:
        request.query_params = kwargs.pop('query_params')
    elif not hasattr(request, 'query_params') and hasattr(request, 'GET'):
        request.query_params = request.GET
    try:
        response = getattr(obj, meth)(request, *args, **kwargs)
    except serializers.ValidationError as e:

        return e.status_code, e.detail
    else:
        return response.status_code, response.data


class MultipleFieldLookupMixin(object):
    def get_object(self):
        cls = self.get_serializer_class().Meta.model
        if hasattr(self, 'kwargs'):
            if self.kwargs:
                if self.kwargs.get('pk'):
                    q = cls.objects.filter(pk=self.kwargs['pk'])
                else:
                    filters = dict((k, self.kwargs[k]) for k in self.lookup_fields if k in self.kwargs)
                    q = cls.objects.filter(**filters)
            else:
                filters = dict((k, self.request.data[k]) for k in self.lookup_fields if k in self.request.data)
                q = cls.objects.filter(**filters)
        else:
            filters = dict((k, self.request.data[k]) for k in self.lookup_fields if k in self.request.data)
            q = cls.objects.filter(**filters)

        return get_object_or_404(q)

    def get_queryset(self):
        cls = self.get_serializer().Meta.model
        return cls.objects.all()

    def get_object_list(self):
        cls = self.get_serializer_class().Meta.model
        if hasattr(self, 'kwargs'):
            if self.kwargs.get('pk'):
                q = cls.objects.filter(pk=self.kwargs['pk'])
            else:
                filters = dict((k, self.kwargs[k]) for k in self.lookup_fields if k in self.kwargs)
                q = cls.objects.filter(**filters)
        else:
            filters = dict((k, self.request[k]) for k in self.lookup_fields if k in self.request)
            q = cls.objects.filter(**filters)

        return get_list_or_404(q)

class UniqueFieldUpdateMixin(object):

    def update(self, request, *args, **kwargs):
        try:
            del request.data['csrfmiddlewaretoken']
        except:
            pass
        if isinstance(request.data, list):
            for d in request.data:
                self.kwargs = d
                q = self._query()
                instance = get_object_or_404(q)
                serializer = self.get_serializer(instance, data=d)
                serializer.is_valid(raise_exception=True)
                q.update(**d)
            return Response('Bulk Update Success!', status=status.HTTP_200_OK)
        elif isinstance(request.data, dict):
            q = self._query()
            instance = get_object_or_404(q)
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            q.update(**request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def _query(self):
        cls = self.get_serializer_class().Meta.model
        if hasattr(self, 'kwargs'):
            if self.kwargs:
                if self.kwargs.get('pk'):
                    q = cls.objects.filter(pk=self.kwargs['pk'])
                else:
                    filters = dict((k, self.kwargs[k]) for k in self.lookup_fields if k in self.kwargs)
                    q = cls.objects.filter(**filters)
            else:
                filters = dict((k, self.request.data[k]) for k in self.lookup_fields if k in self.request.data)
                q = cls.objects.filter(**filters)
        else:
            filters = dict((k, self.request.data[k]) for k in self.lookup_fields if k in self.request.data)
            q = cls.objects.filter(**filters)

        return q

class CreateListModelMixin(object):
    """
    save one or a list model instance.
    """
    # def get_serializer(self, *args, **kwargs):
    #     """ if an array is passed, set serializer to many """
    #     if isinstance(kwargs.get('data', {}), list):
    #         kwargs['many'] = True
    #     return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create_data(self, data, *args, **kwargs):

        serializer = self.get_serializer(data=data, many=isinstance(data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateListModelMixin(object):
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)

        if isinstance(request.data, list):
            for d in request.data:
                self.kwargs = d
                instance = self.get_object()
                serializer = self.get_serializer(instance, data=d, partial=partial)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
            return Response('Bulk Update Success!', status=status.HTTP_200_OK)
        elif isinstance(request.data, dict):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class UpdateDetailMixin(object):
    """
    Update Weekly/PIT/PIT Lite Detail
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)

        if isinstance(request.data, list):
            obj = self.get_serializer_class().Meta.model
            fields = obj._meta.get_all_field_names()
            fields.remove('id')
            for d in request.data:
                filters = {i: d.get(i) for i in self.update_fields}
                week = obj.objects.filter(**filters)
                params = {i: d.get(i) for i in (set(fields) & set(d.keys()))}
                if not week:
                    serializer = self.get_serializer(data=d)
                    if serializer.is_valid():
                        serializer.save()
                else:
                    week.update(**params)

            return Response('Bulk Update Success!', status=status.HTTP_200_OK)

        elif isinstance(request.data, dict):
            try:
                instance = self.get_object()
                serializer = self.get_serializer(instance, data=request.data, partial=partial)
                if serializer.is_valid():
                    self.perform_update(serializer)
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                self.create(request.data, *args, **kwargs)
                return Response(status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class UpdateAfterDestroyMixin(object):
    """
    Destroy old data and create new instead.
    """
    def update(self, request, *args, **kwargs):
        #①三个逻辑，首先确定数据库中是否有该条相同记录，若有则不操作
        #②其次检验是否能创建新数据，若不能，则进行下一步操作
        #③最后更新数据
        if isinstance(request.data, list):
            cls = self.get_serializer_class().Meta.model
            fields = cls._meta.get_all_field_names()
            if 'id' in fields:
                fields.remove('id')
            if request.data:
                for i in request.data:
                    params = {ii: i.get(ii) for ii in (set(fields) & set(i.keys()))}
                    q = cls.objects.filter(**params)
                    if not q:
                        serializer = self.get_serializer(data=params)
                        if serializer.is_valid():
                            serializer.save()
        elif isinstance(request.data, dict):
            cls = self.get_serializer_class().Meta.model
            fields = cls._meta.get_all_field_names()
            if 'id' in fields:
                fields.remove('id')
            if request.data:
                i = request.data
                params = {ii: i.get(ii) for ii in (set(fields) & set(i.keys()))}
                q = cls.objects.filter(**params)
                if not q:
                    serializer = self.get_serializer(data=params)
                    if serializer.is_valid():
                        serializer.save()

        return Response(status=status.HTTP_200_OK)

class DestroyListMixin(object):
    """
    Destroy list model
    """
    def destroy_list(self, request, *args, **kwargs):
        cls = self.get_serializer_class().Meta.model
        instance = cls.objects.filter(**request)
        if instance:
            for i in instance:
                self.perform_destroy(i)
        return Response(status=status.HTTP_204_NO_CONTENT)



class BulkCreateModelMixin(CreateModelMixin):
    """
    Either create a single or many model instances in bulk by using the
    Serializers ``many=True`` ability from Django REST >= 2.2.5.
    .. note::
        This mixin uses the same method to create model instances
        as ``CreateModelMixin`` because both non-bulk and bulk
        requests will use ``POST`` request method.
    """

    def create(self, request, *args, **kwargs):
        bulk = isinstance(request.data, list)

        if not bulk:
            return super(BulkCreateModelMixin, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_bulk_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_bulk_create(self, serializer):
        return self.perform_create(serializer)


class BulkUpdateModelMixin(object):
    """
    Update model instances in bulk by using the Serializers
    """

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        if lookup_url_kwarg in self.kwargs:
            return super(BulkUpdateModelMixin, self).get_object()

        # If the lookup_url_kwarg is not present
        # get_object() is most likely called as part of options()
        # which by default simply checks for object permissions
        # and raises permission denied if necessary.
        # Here we don't need to check for general permissions
        # and can simply return None since general permissions
        # are checked in initial() which always gets executed
        # before any of the API actions (e.g. create, update, etc)
        return None

    def bulk_update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)

        # restrict the update to the filtered queryset
        serializer = self.get_serializer(
            self.filter_queryset(self.get_queryset()),
            data=request.data,
            many=True,
            partial=partial,
        )
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_bulk_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.bulk_update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()

    def perform_bulk_update(self, serializer):
        return self.perform_update(serializer)


class BulkDestroyModelMixin(object):
    """
    Destroy model instances.
    """

    def allow_bulk_destroy(self, qs, filtered):
        """
        Hook to ensure that the bulk destroy should be allowed.
        By default this checks that the destroy is only applied to
        filtered querysets.
        """
        return qs is not filtered

    def bulk_destroy(self, request, *args, **kwargs):
        qs = self.get_queryset()

        filtered = self.filter_queryset(qs)
        if not self.allow_bulk_destroy(qs, filtered):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        self.perform_bulk_destroy(filtered)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def perform_bulk_destroy(self, objects):
        for obj in objects:
            self.perform_destroy(obj)


# class QueryByGuidField(object):
#
#     def query_by_guid(self, request, *args, **kwargs):
#
#         viewset_model = self.get_serializer_class().Meta.model
#         result = []
#         for guid in TestGuid.objects.filter(**request.data):
#             instance_data = list(viewset_model.objects.filter(guid=guid).values())
#             for instance in instance_data:
#                 instance.update({
#                     'year': guid.year,
#                     'ww': guid.ww,
#                     'day': guid.day,
#                     'stack_index': guid.stack_index,
#                     'platform': guid.platform,
#                     'sub_platform': guid.sub_platform
#                 })
#                 del_filed = ['guid_id', 'id']
#                 for _del in del_filed:
#                     del instance[_del]
#             result.extend(instance_data)
#         return Response(data=result, status=status.HTTP_200_OK)
#
#     @list_route(methods=['GET'])
#     def api_guid_query(self, request, *args, **kwargs):
#
#         viewset_model = self.get_serializer_class().Meta.model
#         try:
#             allow_filed = viewset_model.APIMap.API_FIELD
#         except:
#             return Response(data='You are not allowed to access this API', status=status.HTTP_403_FORBIDDEN)
#         result = []
#         filter_dict = {}
#         request_param = ['year', 'ww', 'day', 'platform', 'sub_platform', 'stack_index']
#         for param in request_param:
#             if request.GET.get(param):
#                 filter_dict[param] = request.GET.get(param)
#         for guid in TestGuid.objects.filter(**filter_dict):
#             instance_data = {
#                 'guid': model_to_dict(guid, fields=['year', 'ww', 'day', 'stack_index', 'platform', 'sub_platform']),
#                 'data': viewset_model.objects.filter(guid=guid).values(*allow_filed)
#             }
#             result.append(instance_data)
#         return Response(data=result, status=status.HTTP_200_OK)