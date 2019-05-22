from os.path import dirname, abspath

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
import time
import pyecharts as py
# Create your views here.
from manage_app.models import TZhilianzhaopin
from spider.models import TIp
from django.db.models import Q



def logs(func):
    def write(request):
        with open('log.txt', 'a') as q:
            q.write('ip:' + request.META['REMOTE_ADDR'] + '的用户，在' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '，发送了' + str(request) + '的请求。' + '\n')
        return func(request)
    return write

class pool(object):
    def __init__(self,ip):
        self.ip=ip
    def save(self):
        a=TIp.objects.filter(ip=self.ip)
        if a :
           total=TIp.objects.get(ip=self.ip).total
           ips=TIp.objects.get(ip=self.ip)
           ips.total=total+1
           ips.save()
           print(ips.total)
        else:
            TIp.objects.create(ip=self.ip,total=1)

def spider(func):
    def craw(requset):
        ip=requset.META['REMOTE_ADDR']
        ips=pool(ip).save()
        if TIp.objects.get(ip=ip).total>=100:
            return redirect('gl:yyy')
        else:
            return func(requset)
    return craw

@logs
def code2(request):
    return render(request,'manages/code.html')
@logs
def code3(request):
    ip = request.META['REMOTE_ADDR']
    code=request.session.get('code')
    code2=request.POST.get('code1')
    print(code,code2)
    if code.lower()==code2.lower():
        ips=TIp.objects.get(ip=ip)
        ips.total=0
        ips.save()
        return redirect('gl:sy')
    else:
        return redirect('gl:yyy')



@logs
def home_page(request):

    return render(request,'manages/main.html')
@logs
def introduce(request):

    return render(request,'manages/introduce.html')

@logs
@spider
def menu_page(request):
    name = request.POST.get('fangyuanEntity.fyXqCode')
    second=request.POST.get('fangyuanEntity.fyZldz')
    if name and second:
        if name=='城市':
            list1=TZhilianzhaopin.objects.filter(city=second)
            if second=='北京':
                cityid='3'
            elif second=='上海':
                cityid='4'
            elif second=='广州':
                cityid='5'
            elif second=='深圳':
                cityid='6'
            name=''
        if name=='职位':
            cityid=''
            name=second
            list1=TZhilianzhaopin.objects.filter(position__icontains=second)

    # pie()
    # country()
    else:
        name = request.GET.get('name')
        cityid=request.GET.get('cityid')
        if cityid=='':
            city=''
            list1=TZhilianzhaopin.objects.filter(position__icontains=name)
        else:
            if cityid=='3':
                city='北京'
            elif cityid=='4':
                city='上海'
            elif cityid=='5':
                city = '广州'
            elif cityid=='6':
                city = '深圳'

            list1=TZhilianzhaopin.objects.filter(city=city,position__icontains=name)
    page_count=len(list1)
    num=request.GET.get('num')
    if not num:
        num=1
    ppage=request.POST.get('ppage')
    if ppage:
        num=ppage
    page = Paginator(list1,10).page(int(num))
    cookies = request.COOKIES.get('username')
    if cookies:
        print(78999999)
        return render(request,'manages/menu.html',{'page':page,'page_count':page_count,'cityid':cityid,'name':name})

        return render(request, 'manages/menu.html',{'page': page, 'page_count': page_count, 'cityid': cityid, 'name': name})






# def zhu(request):
#     # attrs=['北京','上海','广州','深圳']
#     # city1=TZhilianzhaopin.objects.filter(city='北京')
#     # city2=TZhilianzhaopin.objects.filter(city='上海')
#     # city3=TZhilianzhaopin.objects.filter(city='广州')
#     # city4=TZhilianzhaopin.objects.filter(city='深圳')
#     # v1=[len(city1),len(city2),len(city3),len(city4)]
#     # bar = py.Bar("柱状图", "各个城市的岗位数量")
#     # bar.add('职位数量',attrs,v1)
#     # bar.render()
#     return render(request,'tables/zhu.html')
@logs
def zhu(request):
    # 柱状图
    # x = ['北京', '上海', '广州', '深圳']
    # bj = TZhilianzhaopin.objects.filter(city='北京').count()
    # sh = TZhilianzhaopin.objects.filter(city='上海').count()
    # gz = TZhilianzhaopin.objects.filter(city='广州').count()
    # sz = TZhilianzhaopin.objects.filter(city='深圳').count()
    # y = [bj, sh, gz, sz]
    # bar = py.Bar('City_count')
    # bar.add('count', x, y)
    # bar.render('zhu.html')
    return render(request,'tables/bar.html')

from pyecharts import Line



def zhexian(request):
    # list2=['web','AI','大数据','爬虫']
    # position1=TZhilianzhaopin.objects.filter(position__icontains='web')
    # position2=TZhilianzhaopin.objects.filter(Q(position__icontains='ai')|Q(position__icontains='人工'))
    # position3=TZhilianzhaopin.objects.filter(position__icontains='大数据')
    # position4=TZhilianzhaopin.objects.filter(position__icontains='爬虫')
    # list1=[len(position1),len(position2),len(position3),len(position4)]
    # line = Line("折线图", "各个岗位的招聘人数")
    # line.add("招聘人数",list2,list1)
    # line.render()
    return render(request,'tables/line.html')
from pyecharts import Map
def pie(request):
    return render(request,'tables/pie.html')
def country():
    map = Map("中国地图", '中国地图', width=1200, height=600)
    provice=['北京','上海','广州','深圳']
    values=[100,200,300,400]
    map.add("", provice, values, visual_range=[0, 50], maptype='china', is_visualmap=True,
            visual_text_color='#000')
    map.show_config()
    return map.render(path="F:\\0000\\spiders\\templates\\tables\\中国地图.html")

