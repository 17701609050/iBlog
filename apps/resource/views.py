# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.resource.models import Resource, ResourceTag, ResourceCategory
from apps.utils.Pager import Page
from apps.blog.models import Category1


class ResourceView(TemplateView, Page):
    template_name = 'resource/resource.html'

    def get_context_data(self, **kwargs):
        context = super(ResourceView, self).get_context_data(**kwargs)
        context['tags'] = ResourceTag.objects.all()
        context['categorys'] = ResourceCategory.objects.all()
        context['category1'] = [cate1 for cate1 in Category1.objects.order_by('add_time')]
        return context

    def get(self, request, *args, **kwargs):
        page_num = request.GET.get('page')

        resources = Resource.objects.prefetch_related('tag').select_related('category')
        context = self.get_context_data()
        if kwargs.get('tag_id'):
            tag = ResourceTag.objects.get(id=kwargs.get('tag_id'))
            resources = resources.filter(tag=tag)
            context['tag'] = tag

        if kwargs.get('category_id'):
            category = ResourceCategory.objects.get(id=kwargs.get('category_id'))
            resources = resources.filter(category=category)
            context['category'] = category

        resources, paginator = self.page(resources, page_num)


        context['obj_infos'] = resources
        context['obj_page_range'] = paginator.page_range
        return self.render_to_response(context)


