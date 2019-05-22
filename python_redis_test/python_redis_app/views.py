import json

from django.shortcuts import render

# Create your views here

from redis import Redis

class Nwe_bi:
    def __init__(self):
        self.name='ytn'
        self.age=18
        self.salary=1

def fun1(a):
    return  a.__dict__



def conn(request):
    conn=Redis(host='192.168.150.128',port=7000)
    user_dump=json.dumps(Nwe_bi(),default=fun1)
    conn.set('objects',user_dump)
    return render(request,'test.html')
if __name__ == '__main__':
    a=Nwe_bi()
    print(a)
    print(a.name)