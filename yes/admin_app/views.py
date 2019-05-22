from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def regist_page(request):
    print('显示成功')
    return HttpResponse(request,'regist.html')