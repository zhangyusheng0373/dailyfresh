from django.contrib import admin
from df_user.models import *

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id','uname']

admin.site.register(UserInfo,UserInfoAdmin)
# Register your models here.
