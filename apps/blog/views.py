#-*- coding: UTF-8 -*-
# Create your views here.

# some function would be used in views
from django.shortcuts import render_to_response
from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog, Tag, Category1, Category2, Profile, \
    Profile_Tag, Friend, Friend_Tag


__category1 = {
    'Geek': '技术博客',
    'Essay': '随笔',
    'Joke': '瞎扯',
    'AAA': 'AAA'
    }
__category2 = {
    'Develop': '开发',
    'Website': 'Web',
    'SRE': '运维',
    'Book': '读书',
    'Movie': '影评',
    'Sports': '运动',
    'Tour': '游记',
    'Joke': '瞎扯'
    }


def __get_latest(objs, max_num=8):

    obj_num = objs.count()
    latest = []

    if obj_num > max_num:
        for i in range(max_num):
            latest.append({'title': objs[i].title, 'id': objs[i].id})
    else:
        for i in range(obj_num):
            latest.append({'title': objs[i].title, 'id': objs[i].id})

    return latest


def aaa():
    pass


def __get_blog_info(objs):

    # exclude blog content!
    blog_info = []

    for blog in objs:
        category1 = blog.category1.category_1
        category2 = blog.category2.category_2
        blog_info.append({
            'title': blog.title,
            'id': blog.id,
            'head_pic_url': blog.head_pic_url,
            'pub_time': blog.pub_time,
            'page_views': blog.page_views,
            'category1': __category1[category1],
            'category2': __category2[category2]})

    return blog_info


# pagination
def __my_pagination(request, objs, display_num=10, after_range=10, before_range=9):
    paginator = Paginator(objs, display_num)

    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    try:
        objects = paginator.page(page)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    except:
        objects = paginator.page(1)

    if page > after_range:
        page_range = paginator.page_range[page-after_range:page+before_range]
    else:
        page_range = paginator.page_range[0:page+before_range]

    return objects, page_range


def __get_blog_list(request, obj_list):
    obj_latest = __get_latest(obj_list)
    obj_infos_all = __get_blog_info(obj_list)
    obj_infos, obj_page_range = __my_pagination(request, obj_infos_all)

    return obj_latest, obj_infos, obj_page_range


def __blog_by_category2(request, objs, category):
    obj_category = Category2.objects.get(category_2=category)
    obj_list = objs.filter(category2=obj_category)
    obj_infos_all = __get_blog_info(obj_list)
    obj_infos, obj_page_range = __my_pagination(request, obj_infos_all)

    return obj_infos, obj_page_range

# the views of the page


def index(request):
    blogs=Blog.objects.all()
    tags=Tag.objects.all()
    latest,blog_infos,page_range=__get_blog_list(request,blogs)
    friends=Friend.objects.all()
    content={'blog_infos':blog_infos,
             'page_range':page_range,
             'tags':tags,
             'latest':latest,
             'friends':friends}
    return render_to_response('index.html', content)

def blog_detail(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    blog.page_views+=1
    blog.save()
    blog_tags=blog.tags.all()
    category1=blog.category1.category_1
    category2=blog.category2.category_2
    category2_url=category1.lower()+'#'+category2
    return render_to_response('detail.html',
                              {'blog':blog,
        'blog_tags':blog_tags,
        'category1':__category1[category1],
        'category2':__category2[category2],
        'category1_url':category1.lower(),
        'category2_url':category2_url
        })


def tag(request,tag_id):

    get_tag=Tag.objects.get(id=tag_id)
    blogs=Blog.objects.filter(tags=get_tag)
    tags=Tag.objects.all()
    tag_latest,tag_infos,page_range=__get_blog_list(request,blogs)
    friends=Friend.objects.all()
    content={'tag_infos':tag_infos,
             'page_range':page_range,
             'tag_latest':tag_latest,
             'get_tag':get_tag,
             'tags':tags,
             'friends':friends}

    return render_to_response('tag.html', content)


def geek(request):

    geek=Category1.objects.get(category_1='geek')
    blogs_geek=Blog.objects.filter(category1=geek)

    tags=Tag.objects.all()

    geek_latest,geek_infos,geek_page_range=__get_blog_list(request,blogs_geek)

    develop_infos,develop_page_range=__blog_by_category2(request,blogs_geek,'Develop')
    website_infos,website_page_range=__blog_by_category2(request,blogs_geek,'website')
    SRE_infos,SRE_page_range=__blog_by_category2(request,blogs_geek,'SRE')

    friends=Friend.objects.all()
    content={'geek_infos':geek_infos,
             'geek_page_range':geek_page_range,
             'develop_infos':develop_infos,
             'develop_page_range':develop_page_range,
             'website_infos':website_infos,
             'website_page_range':website_page_range,
             'SRE_infos':SRE_infos,
             'SRE_page_range':SRE_page_range,
             'geek_latest':geek_latest,
             'tags':tags,
             'friends':friends}

    return render_to_response('geek.html', content)

def essay(request):

    essay=Category1.objects.get(category_1='essay')
    blogs_essay=Blog.objects.filter(category1=essay)

    tags=Tag.objects.all()

    essay_latest,essay_infos,essay_page_range=__get_blog_list(request,blogs_essay)

    book_infos,book_page_range=__blog_by_category2(request,blogs_essay,'book')
    movie_infos,movie_page_range=__blog_by_category2(request,blogs_essay,'movie')
    sports_infos,sports_page_range=__blog_by_category2(request,blogs_essay,'sports')
    tour_infos,tour_page_range=__blog_by_category2(request,blogs_essay,'tour')

    friends=Friend.objects.all()
    content={'essay_infos':essay_infos,
             'essay_page_range':essay_page_range,
             'book_infos':book_infos,
             'book_page_range':book_page_range,
             'movie_infos':movie_infos,
             'movie_page_range':movie_page_range,
             'sports_infos':sports_infos,
             'sports_page_range':sports_page_range,
             'tour_infos':tour_infos,
             'tour_page_range':tour_page_range,
             'essay_latest':essay_latest,
             'tags':tags,
             'friends':friends}

    return render_to_response('essay.html', content)


def joke(request):

    joke=Category2.objects.get(category_2='joke')
    blogs_joke=Blog.objects.filter(category2=joke)

    tags=Tag.objects.all()

    joke_latest,joke_infos,joke_page_range=__get_blog_list(request,blogs_joke)

    friends=Friend.objects.all()
    content={'joke_infos':joke_infos,
             'joke_page_range':joke_page_range,
             'joke_latest':joke_latest,
             'tags':tags,
             'friends':friends}

    return render_to_response('joke.html', content)

def profile(request):
    profile=Profile.objects.get(title='Profile')
    # updates=Profile.objects.get(title='Updates')
    profile_tags=profile.tags.all()
    return render_to_response('profile.html',
                              {'profile':profile,
         # 'updates':updates,
         'profile_tags':profile_tags
        })


