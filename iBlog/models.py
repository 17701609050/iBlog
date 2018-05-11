# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Time    : 18-5-11 下午5:26
# @Author  : Ziping
# @Email   : zipingx.lv@intel.com
# @Project : Automation-Hub
# -----------------------------------------------------

import datetime
from django.db import models

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
