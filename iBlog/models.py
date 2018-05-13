# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Time    : 18-5-11 下午5:26
# @Author  : Ziping
# @Email   : zipingx.lv@intel.com
# @Project : Automation-Hub
# -----------------------------------------------------

import datetime
from django.db import models
from django.contrib.sessions.backends.cache import SessionStore
from django.db.models import Aggregate, CharField

class SysRPermissionUser(models.Model):
    user_name = models.CharField(primary_key=True, max_length=50)
    company_badge = models.CharField(max_length=50, blank=True)
    user_role = models.TextField(blank=True)
    create_time = models.DateTimeField(blank=True, null=True, default=datetime.datetime.utcnow)

    class Meta:
        managed = False
        db_table = 'sys_r_permission_user'

    def __unicode__(self):
        return self.user_name + " " + str(self.company_badge) + " " + str(self.create_time)

class SysMRole(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_code = models.CharField(max_length=16, blank=True)
    role_name_cn = models.CharField(max_length=100, blank=True)
    role_name_en = models.CharField(max_length=100, blank=True)
    role_icon_url = models.CharField(max_length=150, blank=True)
    role_class = models.CharField(max_length=150, blank=True)
    interface_name = models.CharField(max_length=150, blank=True)
    remark = models.CharField(max_length=300, blank=True)

    class Meta:
        managed = False
        db_table = 'sys_m_role'

    def __unicode__(self):
        return self.role_code + " " + self.role_name_cn + " " + self.role_name_en

class SysMFun(models.Model):
    fun_id = models.IntegerField(primary_key=True)
    fun_code = models.CharField(max_length=16, blank=True)
    fun_name_cn = models.CharField(max_length=100, blank=True)
    fun_name_en = models.CharField(max_length=100, blank=True)
    fun_icon_url = models.CharField(max_length=150, blank=True)
    html_id = models.CharField(max_length=100, blank=True)
    fun_class = models.CharField(max_length=150, blank=True)
    remark = models.CharField(max_length=300, blank=True)

    class Meta:
        managed = False
        db_table = 'sys_m_fun'

    def __unicode__(self):
        return self.fun_code + " " + self.fun_name_cn + " " + self.fun_name_en

class SysMMenu(models.Model):
    AUTO_EXPIRE_CHOICES = (
        (0, 'True'),
        (1, 'False'),
    )
    menu_id = models.IntegerField(primary_key=True)
    menu_code = models.CharField(max_length=16, blank=True)
    menu_name_cn = models.CharField(max_length=100, blank=True)
    menu_name_en = models.CharField(max_length=100, blank=True)
    menu_url = models.CharField(max_length=150, blank=True)
    parent_code = models.CharField(max_length=16, blank=True)
    menu_icon_url = models.CharField(max_length=150, blank=True)
    menu_class = models.CharField(max_length=150, blank=True)
    menu_type = models.IntegerField(blank=True, null=True, default=0)
    menu_style = models.CharField(max_length=255, blank=True)
    menu_mark = models.CharField(max_length=25, blank=True)
    menu_config = models.TextField(blank=True, null=True)
    menu_tag = models.CharField(max_length=255, blank=True)
    menu_order_num = models.IntegerField(blank=True, null=True, default=0)
    fun_codes = models.CharField(max_length=300, blank=True)
    recommended = models.IntegerField(default=0, blank=True, null=True)
    visible = models.IntegerField(blank=True, null=True, default=0)
    remark = models.CharField(max_length=300, blank=True)
    auto_expire = models.IntegerField(default=0, choices=AUTO_EXPIRE_CHOICES)
    effective_time_interval = models.IntegerField(null=True)
    last_update_time = models.DateTimeField(null=True)

    class Meta:
        managed = False
        db_table = 'sys_m_menu'

    class Type:
        UNVISIBLE = 0
        VISIBLE = 1

    def __unicode__(self):
        return self.menu_code + " " + self.menu_name_cn + " " + self.menu_name_en

class SysMAuthority(models.Model):
    role_code = models.CharField(max_length=16)
    menu_code = models.CharField(max_length=16)
    fun_codes = models.CharField(max_length=300, blank=True)

    class Meta:
        managed = False
        db_table = 'sys_m_authority'
        unique_together = (("menu_code", "role_code"),)

    def __unicode__(self):
        return self.role_code + " " + self.menu_code + " " + self.fun_codes

class DjLogSessionData(models.Model):
    session_key = models.CharField(primary_key=True, max_length=255)
    session_data = models.TextField(blank=True)

    def get_decoded_data(self):
        try:
            session_data = SessionStore().decode(self.session_data)
        except:
            session_data = {}
        finally:
            return session_data

    def set_encode_data(self, session_dict):
        self.session_data = SessionStore().encode(session_dict)

    class Meta:
        managed = False
        db_table = 'log_session_data'

class GroupConcat(Aggregate):
    # supports COUNT(distinct field)
    function = 'GROUP_CONCAT'
    template = '%(function)s(%(distinct)s%(expressions)s)'

    def __init__(self, expression, distinct=False, **extra):
        super(GroupConcat, self).__init__(
            expression,
            distinct='DISTINCT ' if distinct else '',
            output_field=CharField(),
            **extra)
