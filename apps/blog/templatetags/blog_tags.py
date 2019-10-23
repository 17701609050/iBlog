# -*- coding: UTF-8 -*-
import re
from django import template
from django.utils.html import mark_safe
from ..models import Zan

register = template.Library()


@register.filter(name='get_value')
# get list or dict value
def get_value(value, arg):
    return value[arg]


@register.simple_tag
def highlight_title(text, q):
    '''自定义标题搜索词高亮函数，忽略大小写'''
    if len(q) > 1:
        try:
            text = re.sub(q, lambda a: '<em class="highlighted">{}</em>'.format(a.group()),
                          text, flags=re.IGNORECASE)
            text = mark_safe(text)
        except:
            pass
    return text


@register.simple_tag()
def num():
    try:
        zan_count = 3218 + Zan.objects.all().count()
    except Exception as e:
        zan_count = ''
    return zan_count



