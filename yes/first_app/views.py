from tempfile import template

from django.core.files import temp
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render
from django.template import loader


def hello_world(request):#负责接收并处理浏览器传来的请求
    temp=loader.get_template('你好.html')
    content=temp.render(request=request)
    return HttpResponse(content)