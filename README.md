Django Blog 
===================
该网站为个人的博客网站，用于记录个人的一些技术学习心得及其他东西。
###网站架构
*  **服务器**：空间使用AWS一年免费的虚拟机，使用ubuntu14. 04+Nginx1.8+uWSGI来部署Django应用，从Name.com上购买域名。
*  **博客后台**：修改Django自带的Admin系统，主要添加富文本编辑器用于编写博客，富文本编辑器选择百度的UEditor，其[Django的集成版本](https://github.com/zhangfisher/DjangoUeditor)可以在Github上找到。
*  **网站框架**：Django1.8.19。1.8版较以前版本在Template，staticfiles，数据库同步等方面有一些改动，使用的时候注意参考官方文档。
*  **数据库**：使用MySQL，主要便于同Django集成。
*  **前端**：框架和UI使用Bootstrap3，布局使用Bootstrap的栅格布局，便于做响应式设计，以便支持不同尺寸的设备。使用
SyntaxHighlighter来对pre标签中的代码做代码高亮，目前与Bootstrap似乎还存在一些样式兼容问题。
*设计404页面



**2019.10.20**

    从python从2.7升级到了python3.6,Django1.8.9升级到了Django2.1.7。
    新版本较以前版本改动挺大的，升级的时候遇到一些比较坑的地方。不过最后还是爬过来了，
    学习的过程就是爬坑的过程啊，后续会把升级文章发出来，大家一起爬啊~~~~



**2019.09.05**

    服务器从pythonanywhere.comS搬迁到了阿里云,Centos7.4.1708+Nginx1.12.0+uWSGI来部署
    并从腾讯云买了域名zipinglv.club,地址变为
    www.zipinglv.club
    


**2018.08.30**

    服务器从AWS搬迁到了pythonanywhere.com,地址变为https://zipinglv.pythonanywhere.com
    免费嘛，虽然空间小了点
    
    



