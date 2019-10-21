# -*- coding: UTF-8 -*-
from django import template

register = template.Library()


@register.filter(name='get_movie_name')
# get list or dict value
def get_movie_name(value):
    try:
        movie_name = get_middle_str(value, '《', '》')
    except Exception as e:
        # print str(e)
        movie_name = value
    return movie_name


def get_middle_str(content, start_str, end_str):

    start_index = content.index(start_str)
    end_index = content.index(end_str)

    return content[start_index+1: end_index]


