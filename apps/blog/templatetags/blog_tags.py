# -*- coding: UTF-8 -*-
from django import template
from ..models import Zan

register = template.Library()


@register.filter(name='get_value')
# get list or dict value
def get_value(value, arg):
    return value[arg]


@register.simple_tag()
def num():
    try:
        zan_count = 3218 + Zan.objects.all().count()
    except Exception as e:
        zan_count = ''
    return zan_count



