# -*- coding: utf-8 -*-
import random
from django.shortcuts import render,redirect
from models import Movie, MovieHistory
from forms import MovieInfoForm
from django.views.generic import TemplateView
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from apps.utils.Pager import Page
from .service import movie_service
# Create your views here.


class MovieTemplateMixin(TemplateView, Page):
    template_name = 'movie/movieList.html'
    after_range_num = 5
    before_range_num = 4

    def get_page_num(self, request):
        try:
            page_num = request.GET.get('page')
            if page_num is not None:
                page_num = int(page_num)
            if page_num < 1:
                page_num = 1
        except ValueError:
            page_num = 1
        return page_num

    def get_general_data(self, context):

        context['movie_cate'] = movie_service.movie_cates()[:10]
        context['movie_country'] = movie_service.movie_countrys()[:10]
        context['movie_time'] = movie_service.movie_time
        return context

    def get_page_obj(self, page_num, movies, paginator, context):
        context['obj_infos'] = movies
        if page_num >= self.after_range_num:
            page_range = paginator.page_range[page_num - self.after_range_num:page_num + self.before_range_num]
        else:
            page_range = paginator.page_range[0:int(page_num) + self.before_range_num]
        context['obj_page_range'] = page_range
        return context


class MovieListView(MovieTemplateMixin):

    def get(self, request, *args, **kwargs):

        page_num = self.get_page_num(request)
        movies = Movie.objects.all()
        context = self.get_general_data(self.get_context_data())
        movies, paginator = self.page(movies, page_num)
        context = self.get_page_obj(page_num, movies, paginator, context)
        return self.render_to_response(context)


class MovieSearchView(MovieTemplateMixin):

    def get(self, request, key, *args, **kwargs):
        page_num = self.get_page_num(request)
        movies = Movie.objects.all()
        if key:
            movies = Movie.objects.filter(Q(moviename__contains=key) | Q(actor__contains=key) |
                                          Q(actor__contains=key) | Q(director__contains=key) |
                                          Q(translation_name__contains=key) | Q(chinese_movie_name__contains=key))

        context = self.get_general_data(self.get_context_data())

        movies, paginator = self.page(movies, page_num)

        context = self.get_page_obj(page_num, movies, paginator, context)
        context['search_key'] = key
        return self.render_to_response(context)


class MovieListTypeView(MovieTemplateMixin):

    def get(self, request, style, *args, **kwargs):

        page_num = self.get_page_num(request)

        movies = Movie.objects.filter(style__contains=style).order_by('-doubanscore')
        context = self.get_general_data(self.get_context_data())
        movies, paginator = self.page(movies, page_num)

        context = self.get_page_obj(page_num, movies, paginator, context)
        return self.render_to_response(context)


class MovieListCountryView(MovieTemplateMixin):

    def get(self, request, country, *args, **kwargs):

        page_num = self.get_page_num(request)

        movies = Movie.objects.filter(country__contains=country)
        context = self.get_general_data(self.get_context_data())
        movies, paginator = self.page(movies, page_num)

        return self.render_to_response(self.get_page_obj(page_num, movies, paginator, context))


class MovieListYearView(MovieTemplateMixin):

    def get(self, request, year, *args, **kwargs):

        page_num = self.get_page_num(request)

        movies = Movie.objects.filter(dateyear__contains=year)
        context = self.get_general_data(self.get_context_data())
        movies, paginator = self.page(movies, page_num)

        return self.render_to_response(self.get_page_obj(page_num, movies, paginator, context))


class MovieDoubanView(MovieTemplateMixin):

    def get(self, request, *args, **kwargs):

        page_num = self.get_page_num(request)

        movies = Movie.objects.filter(doubanscore__gte=7).order_by('-doubanscore')
        context = self.get_general_data(self.get_context_data())
        movies, paginator = self.page(movies, page_num)

        return self.render_to_response(self.get_page_obj(page_num, movies, paginator, context))


class MovieImdbView(MovieTemplateMixin):

    def get(self, request, *args, **kwargs):

        page_num = self.get_page_num(request)

        movies = Movie.objects.filter(imdbscore__gte=7).order_by('-imdbscore')
        context = self.get_general_data(self.get_context_data())
        movies, paginator = self.page(movies, page_num)

        return self.render_to_response(self.get_page_obj(page_num, movies, paginator, context))


# 生成历史记录
def generatemoviehistory(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = User.objects.get(pk=1)
    if request.method=='GET':
        movieid = request.GET.get('movieid')
        movie = Movie.objects.get(pk=movieid)
        moviehistory = MovieHistory(user=user,movie=movie,marked=0)
        moviehistory.save()
        return HttpResponse()
    return HttpResponse()


@login_required
def addmovie(request):
    if request.method=='POST':
        form = MovieInfoForm(request.POST,request.FILES)
        if not form.is_valid():
            return render(request,'webuser/addmovie.html',{'form':form})
        else:
            moviename = form.cleaned_data.get('moviename')
            movieaddress = form.cleaned_data.get('movieaddress')
            downloadlink = form.cleaned_data.get('downloadlink')
            style = form.cleaned_data.get('style')
            language = form.cleaned_data.get('language')
            image = request.FILES['image']
            movie = Movie(moviename=moviename,movieaddress=movieaddress,downloadlink=downloadlink,
                          style=style,language=language,image=image,original=str(request.user.webuser.id))
            movie.save()
            messages.add_message(request,messages.SUCCESS,u'电影添加成功.')
    else:
        form = MovieInfoForm();
    return render(request, 'webuser/addmovie.html',{'form':form})


class MovieDetailView(MovieTemplateMixin):
    template_name = 'movie/movieDetail.html'

    def get(self, request, id, *args, **kwargs):
        context = self.get_general_data(self.get_context_data())
        context['movie'] = Movie.objects.get(pk=id)
        return self.render_to_response(context)


