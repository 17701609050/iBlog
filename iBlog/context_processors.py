# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Time    : 19-10-29 上午10:37
# @Author  : Ziping
# @Email   : zipingx.lv@intel.com
# @Project : Automation-Hub
# -----------------------------------------------------

from django.conf import settings


# 自定义上下文管理器
def site_global_variable(request):
    return {
        'query': '',  # 默认全局搜索关键字为空

    }
