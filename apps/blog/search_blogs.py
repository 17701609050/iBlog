# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Time    : 18-7-6 上午10:41
# @Author  : Ziping
# @Email   : 17701609050@163.com
# -----------------------------------------------------
# import requests
# import urllib2
# from pyquery import PyQuery as pq
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
#
# class FindBlogs(object):
#
#     def __init__(self):
#         self.url_index = 'http://zzk-s.cnblogs.com/s/blogpost?Keywords={0}&ViewCount=200&pageindex={1}'
#         self.proxys = {"http": "139.224.80.139:3128"}
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
#             "Cookie": ";"
#             }
#         self.search_content = []
#
#     def search_blogs(self, searchkey, pageindex="1"):
#         result = requests.get(self.url_index.format(searchkey, pageindex), headers=self.headers, proxies=self.proxys)
#         # print result.status_code
#         if result.status_code == 200:
#             self.search_content = result.content.encode('UTF-8')
#         # print self.search_content
#         if self.search_content:
#             return self.parse_html(self.search_content)
#         return self.search_content
#
#     def parse_html(self, search_html):
#         blogs = []
#         doc = pq(search_html)
#         searchItem = doc('#searchResult .searchItem')
#         res = searchItem.items()
#         for item in res:
#             blog_dic = {}
#             blog_dic['id'] = item('h3 a').attr('href')
#             blog_dic['title'] = item('h3 a').text()
#             blog_dic['head_pic_url'] = '/static/img/zipinglx.png'
#             blog_dic['href'] = item('h3 a').attr('href')
#             blog_dic['page_views'] = item('.searchItemInfo .searchItemInfo-views').text()
#             blog_dic['content'] = item('span').text()
#             blog_dic['pub_time'] = item('.searchItemInfo-publishDate').text()
#             blogs.append(blog_dic)
#         return blogs
#
# searchblog = FindBlogs()
#
# if __name__ == "__main__":
#     blog = FindBlogs()
#     search_result = blog.search_blogs("celery")



    # import urllib2
    # import random
    #
    # def url_user_agent(url):
    #     # 设置使用代理
    #     proxy_list = [
    #         {"http": "139.224.80.139"},
    #
    #     ]
    #     proxy = random.choice(proxy_list)
    #     # proxy = {'http': '124.88.67.81:80'}
    #     proxy_support = urllib2.ProxyHandler(proxy)
    #     # opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler(debuglevel=1))
    #     opener = urllib2.build_opener(proxy_support)
    #     urllib2.install_opener(opener)
    #
    #     # 添加头信息，模仿浏览器抓取网页，对付返回403禁止访问的问题
    #     # i_headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    #     i_headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
    #     req = urllib2.Request(url, headers=i_headers)
    #     html = urllib2.urlopen(req)
    #     if url == html.geturl():
    #         doc = html.read()
    #         return doc
    #     return
    #
    #
    # url = 'http://baidu.com'
    # doc = url_user_agent(url)
    # print doc



