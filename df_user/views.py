#coding=utf-8
from hashlib import sha1
from django.shortcuts import render, redirect
from df_user.models import *


def register(request):
    return render(request, 'df_user/register.html')
def register_handle(request):
    post = request.POST
    #获取数据
    uname = post.get('user_name')
    upwd = post.get('pwd')
    uemail=post.get('email')
    #密码加密
    s1=sha1()
    s1.update(upwd)
    upwd3=s1.hexdigest()
    #存储
    user=UserInfo()
    user.uname=uname
    user.upassword=upwd3
    user.uemall=uemail
    user.save()
    return redirect('/user/login/')

def login(request):
    return render(request, 'df_user/login.html')



# Create your views here.
