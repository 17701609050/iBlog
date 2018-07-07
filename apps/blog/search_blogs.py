# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Time    : 18-7-6 上午10:41
# @Author  : Ziping
# @Email   : 17701609050@163.com
# -----------------------------------------------------
import requests
from pyquery import PyQuery as pq
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class FindBlogs(object):

    def __init__(self):
        self.url_index = 'http://zzk-s.cnblogs.com/s/blogpost?Keywords={0}&ViewCount=200&pageindex={1}'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "Cookie": ";"
            }
        self.search_content = []

    def search_blogs(self, searchkey, pageindex="1"):
        result = requests.get(self.url_index.format(searchkey, pageindex), headers=self.headers)
        if result.status_code == 200:
            self.search_content = result.content.encode('UTF-8')
        if self.search_content:
            return self.parse_html(self.search_content)
        return self.search_content

    def parse_html(self, search_html):
        blogs = []
        doc = pq(search_html)
        searchItem = doc('#searchResult .searchItem')
        res = searchItem.items()
        for item in res:
            blog_dic = {}
            blog_dic['id'] = item('h3 a').attr('href')
            blog_dic['title'] = item('h3 a').text()
            blog_dic['head_pic_url'] = '/static/img/zipinglx.png'
            blog_dic['href'] = item('h3 a').attr('href')
            blog_dic['page_views'] = item('.searchItemInfo .searchItemInfo-views').text()
            blog_dic['content'] = item('span').text()
            blog_dic['pub_time'] = item('.searchItemInfo-publishDate').text()
            blogs.append(blog_dic)
        return blogs

searchblog = FindBlogs()

if __name__ == "__main__":
    blog = FindBlogs()
    search_result = blog.search_blogs("celery实例")
    # blogs = blog.parse_html(search_result)



