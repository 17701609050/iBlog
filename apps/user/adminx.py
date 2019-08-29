# -*- coding: UTF-8 -*-
import xadmin
from django.contrib.auth.models import User
from .models import Profile, ProfileTag


class ProfileInline(object):
    model = Profile
    verbose_name_plural = 'profile'


class UserProfileAdmin(object):
    inlines = [ProfileInline]
    # list_display = ('username',)

xadmin.site.unregister(User)
xadmin.site.register(User, UserProfileAdmin)
xadmin.site.register(ProfileTag)

