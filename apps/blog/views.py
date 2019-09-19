# -*- coding: UTF-8 -*-
# Create your views here.

# some function would be used in views
from django.shortcuts import render
from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog, Tag, Category1, Category2, Profile, \
    Profile_Tag, Friend, Friend_Tag, Comment


def index(request):
    # the home page
    __category1 = [cate1 for cate1 in Category1.objects.order_by('add_time')]
    content = {
        'category1': __category1,
    }
    return render(request, 'common/home.html', content)


def baidu_verify_w3IViTxMcb(request):
    # the baidu verify page
    # __category1 = [cate1 for cate1 in Category1.objects.order_by('add_time')]
    # content = {
    #     'category1': __category1,
    # }
    return render(request, 'baidu_verify_w3IViTxMcb.html')


def blog_index(request, blog_url):
    cate2 = request.GET.get("cate2", "")
    # 获取categoty1的所有分类,过滤出cate1的blog
    category1 = [cate1 for cate1 in Category1.objects.order_by('add_time')]
    if blog_url == 'all':
        blogs_list = Blog.objects.all()
        category2 = Category2.objects.all()
    else:
        cate1 = Category1.objects.get(category_1=blog_url)
        blogs_list = Blog.objects.filter(category1=cate1)
        # 过滤出cate2的blog
        category2 = Category2.objects.filter(category1_id=cate1)
    if cate2:
        _category2 = category2.filter(category_2=cate2)
        blogs_list = blogs_list.filter(category2=_category2)

    # 获取最新blogs
    obj_infos_all = __get_blog_info(blogs_list, category1, category2)
    obj_infos, obj_page_range = __my_pagination(request, obj_infos_all)
    obj_latest = __get_latest(blogs_list)

    # 获取所有tag
    tags = Tag.objects.all()
    # 获取外链
    friends = Friend.objects.all()

    content = {
        'obj_infos': obj_infos,
        'obj_page_range': obj_page_range,
        'obj_latest': obj_latest,
        'category1': category1,
        'category2': category2,
        'tags': tags,
        'friends': friends
    }
    return render(request, 'blog/blog_index.html', content)


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


def __get_blog_info(objs, _category1, _category2):
    # exclude blog content!
    blog_info = []

    for blog in objs:
        if len(blog.brief.encode('unicode-escape').decode('string_escape')) > 60:
            content = blog.brief[0:60] + ' ...'
        else:
            content = blog.brief[0:60]
        blog_info.append({
            'title': blog.title,
            'id': blog.id,
            'head_pic_url': blog.head_pic_url,
            'pub_time': blog.pub_time,
            'page_views': blog.page_views,
            'category1': blog.category1.display_name,
            'category2': blog.category2.display_name,
            'content': content,
            'comments': blog.comments.count
        })

    return blog_info


# pagination
def __my_pagination(request, objs, display_num=settings.REST_FRAMEWORK["PAGE_SIZE"], after_range=10, before_range=9):
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

    # if page > after_range:
    #     page_range = paginator.page_range[page - after_range:page + before_range]
    # else:
    #     page_range = paginator.page_range[0:page + before_range]

    return objects, paginator.page_range


def __get_blog_list(request, obj_list):
    obj_latest = __get_latest(obj_list)
    obj_infos_all = __get_blog_info(obj_list)
    obj_infos, obj_page_range = __my_pagination(request, obj_infos_all)

    return obj_latest, obj_infos, obj_page_range


# def __blog_by_category2(request, objs, category):
#     obj_category = Category2.objects.filter(category1_id=category)
#     obj_list = objs.filter(category2=obj_category)
#     obj_infos_all = __get_blog_info(obj_list)
#     obj_infos, obj_page_range = __my_pagination(request, obj_infos_all)
#
#     return obj_infos, obj_page_range


def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.page_views += 1
    blog.save()
    blog_tags = blog.tags.all()
    category1 = blog.category1.category_1
    category2 = blog.category2.category_2
    category2_url = category1.lower() + '#' + category2
    # 为评论引入表单
    comment_form = CommentForm()
    comments = Comment.objects.filter(article_id=blog_id)
    return render(request, 'blog/detail.html',
                              {'blog': blog,
                               'blog_tags': blog_tags,
                               'category1_display_name': blog.category1.display_name,
                               'category1': [cate1 for cate1 in Category1.objects.order_by('add_time')],
                               'category2': blog.category2.display_name,
                               'category1_url': category1.lower(),
                               'category2_url': category2_url,
                               'comments': comments,
                               'comment_form': comment_form,
                               })


def tag(request, tag_id):
    get_tag = Tag.objects.get(id=tag_id)
    blogs = Blog.objects.filter(tags=get_tag)
    category1 = [cate1 for cate1 in Category1.objects.order_by('add_time')]
    category2 = [cate2.category2 for cate2 in blogs]
    obj_infos_all = __get_blog_info(blogs, category1, category2)
    obj_infos, obj_page_range = __my_pagination(request, obj_infos_all)
    obj_latest = __get_latest(blogs)

    tags = Tag.objects.all()
    friends = Friend.objects.all()

    content = {
        'obj_infos': obj_infos,
        'obj_page_range': obj_page_range,
        'obj_latest': obj_latest,
        'category1': category1,
        'category2': category2,
        'tags': tags,
        'get_tag': get_tag,
        'friends': friends
    }

    return render(request, 'blog/tag.html', content)


def profile(request):
    __category1 = [cate1 for cate1 in Category1.objects.order_by('add_time')]
    pro_file = Profile.objects.all()[0]
    # updates=Profile.objects.get(title='Updates')
    profile_tags = pro_file.tags.all()
    return render(request, 'common/profile.html',
                              {'profile': pro_file,
                               # 'updates':updates,
                               'profile_tags': profile_tags,
                               'category1': __category1,
                               })


def post_comment(request, blog_id, parent_comment_id=None):
    article = get_object_or_404(Blog, id=blog_id)

    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if not request.user.username:
            redirect_url = '/user/login/?targetUri=/blog/blog_detail/blog_'+blog_id
            return redirect(redirect_url)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user

            # 二级回复
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                # 若回复层级超过二级，则转换为二级
                new_comment.parent_id = parent_comment.get_root().id
                # 被回复人
                new_comment.reply_to = parent_comment.user
                new_comment.save()

                # 给其他用户发送通知
                # if not parent_comment.user.is_superuser and not parent_comment.user == request.user:
                #     notify.send(
                #         request.user,
                #         recipient=parent_comment.user,
                #         verb='回复了你',
                #         target=article,
                #         action_object=new_comment,
                #     )

                # return HttpResponse("200 OK")
                return JsonResponse({"code": "200 OK", "new_comment_id": new_comment.id})

            new_comment.save()

            # 给管理员发送通知
            # if not request.user.is_superuser:
                # notify.send(
                #     request.user,
                #     recipient=User.objects.filter(is_superuser=1),
                #     verb='回复了你',
                #     target=article,
                #     action_object=new_comment,
                # )

            # 添加锚点
            redirect_url = '/blog/blog_detail/blog_'+blog_id + '#comment_elem_' + str(new_comment.id)
            return redirect(redirect_url)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理 GET 请求
    elif request.method == 'GET':
        comment_form = CommentForm()
        context = {
            'comment_form': comment_form,
            'article_id': blog_id,
            'parent_comment_id': parent_comment_id
        }
        return render(request, 'blog/reply.html', context)
    # 处理其他请求
    else:
        return HttpResponse("仅接受GET/POST请求。")