# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Time    : 18-7-6 上午10:41
# @Author  : Ziping
# @Email   : zipingx.lv@intel.com
# @Project : Automation-Hub
# -----------------------------------------------------
import requests
from pyquery import PyQuery as pq


class FindBlogs(object):

    def __init__(self):
        self.url_index = 'http://zzk-s.cnblogs.com/s/blogpost?Keywords='
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "Cookie": ";"
            }
        self.search_content = None

    def search_blogs(self, searchkey):
        result = requests.get(self.url_index+searchkey, headers=self.headers)
        if result.status_code == 200:
            self.search_content = result.content
        return self.search_content

    def parse_html(self, search_html):
        blogs = []
        if search_html:
            doc = pq(search_html)
            searchItem = doc('#searchResult .searchItem')
            res = searchItem.items()
            for item in res:
                blog_dic = {}
                blog_dic['text'] = item('h3 a').text()
                blog_dic['href'] = item('h3 a').attr('href')
                blog_dic['content'] = item('span').text()
                blogs.append(blog_dic)
            import pprint
            pprint.pprint(blogs)
        return blogs


if __name__ == "__main__":
    blog = FindBlogs()
    search_result = blog.search_blogs("django-middleware")
    blogs = blog.parse_html(search_result)



