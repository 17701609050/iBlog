Django Blog 
===================
该网站为个人的博客网站，用于记录个人的一些技术学习心得及其他东西。
###网站架构
* **服务器**：空间使用AWS一年免费的虚拟机，使用ubuntu14. 04+Nginx1.8+uWSGI来部署Django应用，从Name.com上购买域名。
*  **博客后台**：修改Django自带的Admin系统，主要添加富文本编辑器用于编写博客，富文本编辑器选择百度的UEditor，其[Django的集成版本](https://github.com/zhangfisher/DjangoUeditor)可以在Github上找到。
*  **网站框架**：Django1.8.19。1.8版较以前版本在Template，staticfiles，数据库同步等方面有一些改动，使用的时候注意参考官方文档。
*  **数据库**：使用MySQL，主要便于同Django集成。
*  **前端**：框架和UI使用Bootstrap3，布局使用Bootstrap的栅格布局，便于做响应式设计，以便支持不同尺寸的设备。使用
SyntaxHighlighter来对pre标签中的代码做代码高亮，目前与Bootstrap似乎还存在一些样式兼容问题。
*设计404页面



