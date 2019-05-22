

import MySQLdb
from MySQLdb.cursors import DictCursor
from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse

from django.shortcuts import render, redirect


# Create your views here.
# 显示首页界面
from task_app.models import task


def emplist_page(request):
    num=request.GET.get('num')
    print(num)
    if not num:
        num=1
    print(num)
    paginator = Paginator(object_list=task.objects.all(), per_page=3)
    page=paginator.page(num)
    # conn = MySQLdb.connect(
    #     host='localhost',
    #     port=3306,
    #     user='root',
    #     db='mysql_db',
    #     password='123456',
    #     charset='utf8'
    # )
    # cursor=conn.cursor(DictCursor)
    # sql='select id,name,salary,age,gender,birth from employee'
    # cursor.execute(sql)
    # result=cursor.fetchall()
    a=request.session.get('succ')

    if a:
        user=task.objects.all()
        return render(request,'task/emplist.html',{'tuple':user,'page':page})
    else:
        return redirect('yh:dljm')






#添加用户信息：
# 点击显示添加界面
def user_add_page(request):
    return render(request,'task/addEmp.html')

#点击添加成功
def user_add(request):
    name=request.POST.get('name')
    salary=request.POST.get('salary')
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    birth=request.POST.get('birth')
    pic=request.FILES.get('file1')
    # conn = MySQLdb.connect(
    #     host='localhost',
    #     port=3306,
    #     user='root',
    #     db='mysql_db',
    #     password='123456',
    #     charset='utf8'
    # )
    # cursor = conn.cursor(DictCursor)
    # sql='insert into employee(name,salary,age,gender,birth) values (%s,%s,%s,%s,%s)'
    # cursor.execute(sql,(name,salary,age,gender,birth))
    # conn.commit()
    # cursor.close()
    # conn.close()
    try:
        with transaction.atomic():
            task.objects.create(name=name, salary=salary, age=age, gender=gender, birth=birth, pic1=pic)
            print('niub i1')
            return HttpResponse('ok')

    except:
        print(2)
        return HttpResponse('error')

#显示图片





# 点击删除一行，且有弹窗：
def delete(request):
    # conn = MySQLdb.connect(
    #     #     host='localhost',
    #     #     port=3306,
    #     #     user='root',
    #     #     db='mysql_db',
    #     #     password='123456',
    #     #     charset='utf8'
    #     # )
    id=request.GET.get('id')
    #     # cursor = conn.cursor(DictCursor)
    #     # sql='delete from employee where id=%s'
    #     # cursor.execute(sql,(id,))
    #     # conn.commit()
    #     # cursor.close()
    #     # conn.close()
    task.objects.get(id=id).delete()
    return redirect('gl:syjm')



#点击更新转到更新页面：
def update_page(request):
    # conn = MySQLdb.connect(
    #     host='localhost',
    #     port=3306,
    #     user='root',
    #     db='mysql_db',
    #     password='123456',
    #     charset='utf8'
    # )
    id = request.GET.get('id')
    # cursor = conn.cursor(DictCursor)
    # sql='select * from employee where id =%s'
    # cursor.execute(sql,(id,))
    # result=cursor.fetchone()
    result=task.objects.get(id=id)
    return render(request,'task/updateEmp.html',{'object':result})




# 点击获得更新后的信息传回表中
def update1(request):
    id = request.GET.get('id')
    name = request.POST.get('name')
    salary = request.POST.get('salary')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    birth = request.POST.get('birth')
    # conn = MySQLdb.connect(
    #     host='localhost',
    #     port=3306,
    #     user='root',
    #     db='mysql_db',
    #     password='123456',
    #     charset='utf8'
    # )
    # cursor = conn.cursor(DictCursor)
    # sql='update employee set name=%s,salary=%s,age=%s,gender=%s,birth=%s where id=%s'
    # cursor.execute(sql,(name,salary,age,gender,birth,id))
    # conn.commit()
    # cursor.close()
    # conn.close()
    user=task.objects.get(id=id)
    user.name=name
    user.salary=salary
    user.age=age
    user.gender=gender
    user.birth=birth
    user.save()
    return redirect('gl:syjm')


