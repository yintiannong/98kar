import MySQLdb
from MySQLdb.cursors import DictCursor
from django.shortcuts import render, redirect


# Create your views here.

def show(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='mysql_db',
        charset='utf8')
    cursor = conn.cursor(DictCursor)
    sql='select id,name,salary,age,gender,birth from employee'
    cursor.execute(sql)
    result=cursor.fetchall()
    return render(request,'emplist.html',{'tuple':result})



def addemp_page(request):
    return render(request,'addEmp.html')


def addemp_page_onclik(request):
    name=request.POST.get('name')
    salary=request.POST.get('salary')
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    birth=request.POST.get('birth')
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='mysql_db',
        charset='utf8')
    cursor = conn.cursor(DictCursor)
    sql='insert into employee(name,salary,age,gender,birth) values(%s,%s,%s,%s,%s) '
    cursor.execute(sql,(name,int(salary),int(age),int(gender),birth))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('admin1:show1')

def dele(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='mysql_db',
        charset='utf8')
    id=request.GET.get('id')
    cursor = conn.cursor(DictCursor)
    sql='delete from employee where id=%s'
    cursor.execute(sql,(id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('admin1:show1')




def update(request):

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='mysql_db',
        charset='utf8')
    id = request.GET.get('id')
    cursor = conn.cursor(DictCursor)
    sql='select id, name,salary,age,gender,birth from employee where id=%s'
    cursor.execute(sql,(id))
    result=cursor.fetchone()
    return render(request,'updateEmp.html',result)


def update_r(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='mysql_db',
        charset='utf8')
    id = request.GET.get('id')
    cursor = conn.cursor(DictCursor)
    name=request.POST.get('name')
    salary=request.POST.get('salary')
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    birth=request.POST.get('birth')
    sql='update employee set name=%s,salary=%s,age=%s,gender=%s,birth=%s where id=%s'
    cursor.execute(sql,(name,salary,age,gender,birth,id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('admin1:show1')

