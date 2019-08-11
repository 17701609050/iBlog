# -*- coding: UTF-8 -*-
from django import template

register = template.Library()


@register.filter(name='get_value')
# get list or dict value
def get_value(value):
    tag_list = []
    for tag in value._prefetched_objects_cache['tag']:
        tag_list.append(tag.tag)
    return ', '.join(tag_list)





