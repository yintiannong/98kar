from django.http import HttpResponse
from django.shortcuts import render, redirect
import uuid
# Create your views here.
import happybase

from job1_app.models import Save




def regist_page(request):
    return render(request,'regist.html')


def regist(request):
    connection = happybase.Connection(host='192.168.197.24', port=9090)
    connection.open()
    username=request.POST.get('username')
    password=request.POST.get('password')
    province=request.POST.get('province')
    city=request.POST.get('city')
    birth=request.POST.get('birth')
    uuids=uuid.uuid1()
    table = connection.table('job1:t_user')
    table.put(str(uuids), {'people:username': username,'people:password':password,'people:birth':birth,'other:province':province,'other:city':city})
    return HttpResponse('注册成功')

def btos(c): ##输入的c是 c=list(table.scan())
    '''将HBase的scan输出的二进制字符串转为普通字符串'''
    d = []
    for i in c:
        i = list(i)
        i[0] = i[0].decode()
        dict2 = {}
        for j in i[1]:

            j1=j.decode()
            list3=''
            for key in j1:
                if key!=':':
                    list3+=key
            j1=list3
            print(j1)
            i[1][j] = (i[1].get(j)).decode()
            dict2[j1]=i[1][j]
            print(dict2)

        d.append((i[0],dict2))
    return d

def list_page(request):

    connection = happybase.Connection(host='192.168.197.24', port=9090)
    connection.open()

    table = connection.table('job1:t_user')
    print('mdfmksfmd')
    print(table)
    c=list(table.scan())
    print(c)
    d=btos(c)
    # def convert(data):
    #     if isinstance(data,list):
    #         print(1)
    #         for i in data :
    #             return
    #     if isinstance(data, bytes):
    #         print(2)
    #         return data.decode()
    #     if isinstance(data, dict):
    #         print(3)
    #         return dict(map(convert, data.items()))
    #     if isinstance(data, tuple):
    #         print(4)
    #         for j in data:
    #             convert(j)
    #     return data
    # d=convert(c)
    print(d)
    return render(request,'userlist.html',{'list1':d})




def result_page(request):
    list1=Save.objects.filter()
    print(list1)
    return render(request,'result.html',{'list1':list1})


def dels(request):
    id=request.GET.get('id')
    connection = happybase.Connection(host='192.168.197.24', port=9090)
    connection.open()

    table = connection.table('job1:t_user')
    table.delete(id);
    return redirect('list')