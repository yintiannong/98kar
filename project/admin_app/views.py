import os
import random
import string
import time

import MySQLdb
from MySQLdb.cursors import DictCursor
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

# 用户的注册页面显示;
from admin_app.image import ImageCaptcha
from admin_app.models import Admin

def pd_yzm(request):
    time.sleep(2)
    num=request.GET.get('num')
    a=request.session.get('code')
    print(num,a)
    if num.lower() == a.lower():
        return HttpResponse('ok')
    else:
        return HttpResponse('error')


def yzm(request):
    image = ImageCaptcha(fonts=[os.path.abspath('fonts/segoescb.ttf')]) #代表当前路径后的啥

    code = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 5)

    request.session['code'] = ''.join(code)
    data = image.generate(''.join(code))
    print(code)
    return HttpResponse(data,'image/png')

def regist_page(request):
    return render(request,'admin/regist.html')


def username_yz(request):
    time.sleep(2)
    username=request.GET.get('username')
    a=Admin.objects.filter(username=username)
    if a:
        request.session['nb']='nb'
        return HttpResponse('error')
    else:
        return HttpResponse('ok')





#用户注册提交信息
def regist(request):
#生成验证码图片
    yzm=request.POST.get('number')
    username=request.POST.get('username')
    name=request.POST.get('name')
    pwd=request.POST.get('pwd')
    password=make_password(pwd)
    sex=request.POST.get('sex')
    birth=request.POST.get('birth')
    # conn=MySQLdb.connect(
    #     host='localhost',
    #     port=3306,
    #     user='root',
    #     password='123456',
    #     db='mysql_db',
    #     charset='utf8'
    # )
    # cursor=conn.cursor()
    # sql='insert into admin_t(username,name,password,sex,birth) values (%s,%s,%s,%s,%s)'
    # cursor.execute(sql,(username,name,pwd,sex,birth))
    # conn.commit()
    # cursor.close()
    # conn.close()
    sjk=request.session.get('code')
    if yzm.lower()==sjk.lower():
        Admin.objects.create(username=username,name=name,password=password,sex=sex,birth=birth)
        return redirect('yh:dljm')
    else:
        return render(request,'admin/regist.html')

#显示登录界面


def login_page(request):
    try:
        content=request.session.get('name1')
        username1=request.COOKIES.get('username')
        username=str(username1.encode('latin-1'),'utf-8')
        # username=request.session.get('username')
        if content:

            del request.session['name1']

            return render(request, 'admin/login.html', {'username': username, 'content': content})
        else:
            return render(request,'admin/login.html',{'username':username})
    except:
        print('co')
#登录

def login(request):
    username=request.POST.get('name')
    password=request.POST.get('pwd')
    # conn = MySQLdb.connect(
    #     host='localhost',
    #     port=3306,
    #     user='root',
    #     password='123456',
    #     db='mysql_db',
    #     charset='utf8'32dsdsea
    # )
    # cursor = conn.cursor(DictCursor)
    # sql='select id from admin_t where username=%s and password=%s'
    # cursor.execute(sql,(username,password))
    # result=cursor.fetchone()
    # if result:
    #     return redirect('gl:syjm')
    a=request.POST.get('username1')
    admin = Admin.objects.filter(username=username).values('password')[0].get('password')
    content = redirect('gl:syjm')
    if check_password(password,admin):
        request.session['succ']='niubi'

        if a:
            content.set_cookie('username', str(username.encode('utf-8'), 'latin-1'), max_age=60 * 60 * 24 * 7)
            # request.session['username']=username
            return content
            # return content
        return content
    else:
        request.session['name1']='用户名或密码错误！请重新登录'
        return redirect('yh:dljm')




