# -*- coding: UTF-8 -*-
__author__ = 'zipinglv'
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^movie-list/$', views.MovieListView.as_view(), name='movie_list'),
    url(r'^movie-search/(?P<key>.+)/$', views.MovieSearchView.as_view(), name='movie_search'),
    url(r'^movie-list/type/(?P<style>.+)/$', views.MovieListTypeView.as_view(), name='movie_list_type'),
    url(r'^movie-list/country/(?P<country>.+)/$', views.MovieListCountryView.as_view(), name='movie_list_country'),
    url(r'^movie-list/year/(?P<year>.+)/$', views.MovieListYearView.as_view(), name='movie_list_year'),
    url(r'^movie-list/douban-high-score/$', views.MovieDoubanView.as_view(), name='movie_list_douban'),
    url(r'^movie-list/imdb-high-score/$', views.MovieImdbView.as_view(), name='movie_list_imdb'),

    # url(r'^getmovielistbystyle/$',views.getmovielistbystyle,name='getmovielistbystyle'),
    # url(r'^getmovielist/(?P<page>\d*)/$',views.getmovielist,name='getmovielist'),
    # url(r'^getmovielist/(\d+)/$', views.getmovielist, name='getmovielist'),
    # url(r'^getlatestmovielist/$', views.getlatestmovielist, name='getlatestmovielist'),
    # url(r'^getlatestmovielist/(\d+)/$', views.getlatestmovielist, name='getlatestmovielist'),
    # url(r'^getfilmfestlist/$', views.getfilmfestlist, name='getfilmfestlist'),
    # url(r'^getfilmfestlist/(\d+)/$', views.getfilmfestlist, name='getfilmfestlist'),
    # url(r'^generatemoviehistory', views.generatemoviehistory, name='generatemoviehistory'),
    # url(r'^searchmovie/$', views.searchmovie,name='searchmovie'),
    url(r'^addmovie/$', views.addmovie, name='addmovie'),
    url(r'^movie-detail/(?P<id>\w+)/$', views.MovieDetailView.as_view(), name='movie_detail'),
]