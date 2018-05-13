# -*- coding: utf-8 -*-
"""
@Created middleware.py on 16-4-21 PM4:43
@Author: Gaobo.Xiao
@Version: V2
@license: Intel-ICG
"""
from django.http.response import HttpResponseRedirect
from django.core.cache import cache

from .login_service import do_login
from .service import SessionArgs, DjLogLoginService, url_reverse, url_rules_match
# from apps.api.utils import url_rules_match, url_reverse, SessionArgs, USER_BLACKLIST
#
# from apps.api.utils import get_ip_address


class SessionInterceptor(object):

    def process_request(self, req):
        """
        1:条件：当前请求路径不属于登录相关路径
        2:条件：当前请求路径不属于静态文件相关路径
        3:条件：当前请求路径不属于API访问相关路径
        4:条件：当前请求路径不属于游客访问相关路径
                     以上条件均满足时，需要判断当前用户是否已登录或者曾经登录
        """
        # 拦截异常用户
        # * 1： 拦截所有
        # user_blacklist = cache.get(SessionArgs.USER_BLACKLIST_PREFIX + req.user.username, [])
        # if user_blacklist == "*":
        #     return HttpResponseRedirect(url_reverse('tourist', kwargs={'page_name': '403'}))
        # # * 2： 拦截固定URL
        # if req.REQUEST.get('user_name') in USER_BLACKLIST or req.user.username in USER_BLACKLIST or \
        #                         req.get_full_path()+';' in user_blacklist:
        #     return HttpResponseRedirect(url_reverse('tourist', kwargs={'page_name': '403'}))

        if url_rules_match(req):
            # 1: 记录拦截前地址
            redirect_url = url_reverse('login')
            if req.get_full_path() != '/':
                redirect_url += '#*redirecturl*='+req.get_full_path()

            # 2: 已登录检查
            is_logined = False
            if not req.user.is_authenticated():
                (is_auth, session_data) = do_login(req)
                is_logined = True
                if not is_auth:
                    return HttpResponseRedirect(redirect_url)
                else:
                    req.session_data = session_data

            # 3: 加载Session data
            if not hasattr(req, 'session_data'):
                loginservice = DjLogLoginService(None)
                session_data = loginservice.getSessionData(req)
                if session_data is None:
                    # IDSID 自动登录
                    if not is_logined and req.COOKIES.get(SessionArgs.STAFF_TOKEN) is not None:
                        (is_auth, session_data) = do_login(req, manual=False)
                        if not is_auth:
                            return HttpResponseRedirect(redirect_url)
                        else:
                            req.session_data = session_data
                    else:
                        return HttpResponseRedirect(redirect_url)
                else:
                    req.session_data = session_data

            # 4: 已登录没有目地请求
            if req.path == '/':
                return HttpResponseRedirect(url_reverse('home'))
            else:
                if not req.is_ajax() and req.method == 'GET':  # not ajax/post/put/delete log
                    pass
                    # djLogLoginService.logUserVisitHistory(req.user.username, req.get_full_path(), get_ip_address(req))


