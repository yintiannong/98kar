from MySQLdb.cursors import DictCursor
from django.http import request, HttpResponse
from django.shortcuts import render
import MySQLdb
# Create your views here.
from django.template import loader


def serch_user(request):

    conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        db='mysql_db',
        user='root',
        password='123456',
        charset='utf8')
    cursor=conn.cursor(DictCursor)
    sql='select id ,name from user '
    cursor.execute(sql)
    c=cursor.fetchone()

    # tem = loader.get_template('user.html')
    #
    # content = tem.render(c,request=request)
    # return HttpResponse(content)
    return render(request,'user.html',c)
