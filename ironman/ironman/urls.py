"""ironman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from job1_app.views import regist_page, regist, list_page, result_page, dels

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regist_page/',regist_page,name='zcjm'),
    path('regist/',regist,name='zc'),
    path('list/',list_page,name='list'),
    path('result_page/',result_page,name='jg'),
    path('dels/',dels,name='sc')
]