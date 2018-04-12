#coding=utf-8
from hashlib import sha1
from . import user_decorator
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from df_user.models import *
from df_goods.models import *


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
    uname=request.COOKIES.get('uname','')
    context={'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request, 'df_user/login.html',context)

def login_handle(request):
    post=request.POST
    uname=post.get('username')
    upwd=post.get('pwd')
    rember=post.get('rember',0)
    users=UserInfo.objects.filter(uname=uname)
    #判断用户名
    if len(users)==1:
        s1=sha1()
        s1.update(upwd)
        if s1.hexdigest()==users[0].upassword:
            red = HttpResponseRedirect('/user/info')
            #判断是否记住用户名
            if rember!=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            return red
        else:
            context={'title':'用户登录','error_name': 0,'error_pwd': 1,'uname':uname,'pwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        context={'title':'用户登录','error_name': 1,'error_pwd': 0,'uname':uname,'pwd':upwd}
        return render(request,'df_user/login.html',context)

def logout(requset):
    requset.session.flush()
    return redirect('/')

def register_exist(requset):
    uname = requset.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

@user_decorator.login
def info(request):
    user_email=UserInfo.objects.get(id=request.session['user_id']).uemall
    #最近浏览
    goods_ids=request.COOKIES.get('goods_ids','')
    goods_ids1=goods_ids.split(',')
    goods_list=[]
    if goods_ids1[0]!='':
        for goods_id in goods_ids1:
            goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

    context={
        'title':'用户中心',
        'user_email':user_email,
        'user_name':request.session['user_name'],
        'goods_list':goods_list,}
    return render(request,'df_user/user_center_info.html',context)

@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method=='POST':
        post=request.POST
        user.ushou=post.get('ushou')
        user.uaddress=post.get('uaddress')
        user.uyoubian=post.get('uyoubian')
        user.uphoto=post.get('uphone')
        user.save()
    context={'title':'用户中心','user':user,}
    return render(request,'df_user/user_center_site.html', context)

# Create your views here.
