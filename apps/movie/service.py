# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Time    : 19-9-9 下午5:08
# @Author  : Ziping
# @Email   : zipingx.lv@intel.com
# -----------------------------------------------------
from django.db.models import Count
from .models import Movie


class MovieService(object):

    def movie_cates(self):
        cates = Movie.objects.all().values('style').annotate(count=Count('style'))
        movie_cate = []
        for cate in cates:
            style_list = cate['style'].replace(' ', '').split('/')
            for style in style_list:
                if style not in movie_cate:
                    movie_cate.append(style)
        return movie_cate
        # movie_cate = ['剧情', '动作', '武侠', '爱情', '悬疑', '恐怖', '犯罪', '冒险', '惊悚', '战争', '灾难', '喜剧', '科幻', '动画',
        #               '纪录片', '传记', '历史', '情色', '其他']

    def movie_countrys(self):
        countrys = Movie.objects.all().values('country').annotate(count=Count('country'))
        movie_country = []
        for country in countrys:
            country_list = country['country'].replace(' ', '').split('/')
            for cl in country_list:
                if cl not in movie_country:
                    movie_country.append(cl)
        return movie_country
        # movie_country = ['中国', '香港', '台湾', '美国', '日本', '韩国', '欧洲', '英国', '德国', '法国', '泰国', '印度', '意大利',
        #                  '瑞典', '其他']

    movie_time = ['2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008',
                  '2007', '2006', '2005', '2004', '2003', '2002', '2001', '2000']


movie_service = MovieService()

