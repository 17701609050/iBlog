# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Time    : 18-7-6 上午10:41
# @Author  : Ziping
# @Email   : zipingx.lv@intel.com
# @Project : Automation-Hub
# -----------------------------------------------------
import requests


class FindBlogs(object):

    def __init__(self):
        self.url_index = 'http://zzk-s.cnblogs.com/s/blogpost?Keywords='
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "Cookie": ";"
            }

    def search_blogs(self, searchkey):
        content = []
        result = requests.get(self.url_index+searchkey, headers=self.headers)
        if result.status_code == 200:
            print result.content
            content = result.content
        return content


if __name__ == "__main__":
    blog = FindBlogs()
    blog.search_blogs("django-middleware")

