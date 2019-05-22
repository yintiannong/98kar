import MySQLdb
from MySQLdb.cursors import DictCursor
from django.shortcuts import render, redirect


# Create your views here.
def regist_page(request):
    print('显示成功')
    return render(request,'regist.html')

def regist_onclik(request):
    user_name=request.POST.get('username')
    rel_name=request.POST.get('name')
    password=request.POST.get('password')
    sex=request.POST.get('sex')
    birth=request.POST.get('birth')
    conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='mysql_db',
        charset='utf8'
    )
    cursor=conn.cursor(DictCursor)
    sql='insert into admin_t(username,name,password,sex,birth) values (%s,%s,%s,%s,%s)'
    cursor.execute(sql,(user_name,rel_name,password,sex,birth))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/login/")
def login_page(request):
    return render(request, 'login.html')

def login(request):
    user_name=request.POST.get('name')
    password=request.POST.get('pwd')
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='mysql_db',
        charset='utf8')
    cursor = conn.cursor(DictCursor)
    sql='select id from admin_t where username=%s and password=%s'
    cursor.execute(sql,(user_name,password))
    sql_content=cursor.fetchone()
    if sql_content:
        return redirect('admin1:show1')
    return redirect('/login/')


