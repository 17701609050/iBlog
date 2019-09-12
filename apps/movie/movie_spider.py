# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Time    : 19-9-9 下午3:15
# @Author  : Ziping
# @Email   : zipingx.lv@intel.com
# -----------------------------------------------------
from bs4 import BeautifulSoup
import requests
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def get_html(web_url):  # 爬虫获取网页没啥好说的
    header = {
        "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
    html = requests.get(url=web_url, headers=header).text#不加text返回的是response，加了返回的是字符串
    Soup = BeautifulSoup(html, "lxml")
    data = Soup.find("ol").find_all("li")  # 还是有一点要说，就是返回的信息最好只有你需要的那部分，所以这里进行了筛选
    return data


def get_info(all_move):
    f = open("/home/zipinglx/project/douban.txt", "a")

    for info in all_move:
        #    排名
        nums = info.find('em')
        num = nums.get_text()

        #    名字
        names = info.find("span")  # 名字比较简单 直接获取第一个span就是
        name = names.get_text()

        #    导演
        charactors = info.find("p")  # 这段信息中有太多非法符号你需要替换掉
        charactor = charactors.get_text().replace(" ", "").replace("\n", "")  # 使信息排列规律
        # charactor = charactor.replace("\xa0", "").replace("\xee", "").replace("\xf6", "").replace("\u0161", "").replace(
        #     "\xf4", "").replace("\xfb", "").replace("\u2027", "").replace("\xe5", "")

        #    评语
        remarks = info.find_all("span", {"class": "inq"})
        if remarks:  # 这个判断是因为有的电影没有评语，你需要做判断
            remark = remarks[0].get_text().replace("\u22ef", "")
        else:
            remark = "此影片没有评价"
        print(remarks)

        # 评分
        scores = info.find_all("span", {"class": "rating_num"})
        score = scores[0].get_text()

        f.write(num + '、')
        f.write(name + "\n")
        f.write(charactor + "\n")
        f.write(remark + "\n")
        f.write(score)
        f.write("\n\n")

    f.close()  # 记得关闭文件


if __name__ == "__main__":
    # if os.path.exists("/home/zipinglx/project/") == False:  # 两个if来判断是否文件路径存在 新建文件夹 删除文件
    #     os.mkdir("/home/zipinglx/project/")
    # if os.path.exists("/home/zipinglx/project/douban.txt") == True:
    #     os.remove("/home/zipinglx/project/douban.txt")
    #
    # page = 0  # 初始化页数，TOP一共有250部   每页25部
    # while page <= 225:
    #     web_url = "https://movie.douban.com/top250?start=%s&filter=" % page
    #     all_move = get_html(web_url)  # 返回每一页的网页
    #     get_info(all_move)  # 匹配对应信息存入本地
    #     page += 25
    # encoding=utf-8
    import jieba
    seg_list = jieba.cut("我来到北京清华大学", cut_all = True)
    print "Full Mode:", "/ ".join(seg_list) #  全模式
    seg_list = jieba.cut("我来到北京清华大学", cut_all = False)
    print "Default Mode:", "/ ".join(seg_list) #  精确模式
    seg_list = jieba.cut("他来到了网易杭研大厦") #  默认是精确模式
    print ", ".join(seg_list)
    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造") #  搜索引擎模式
    print ", ".join(seg_list)
