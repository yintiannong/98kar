from django.urls import path

from admin_app.views import regist_page, regist, login_page, login, yzm, username_yz, pd_yzm

urlpatterns = [
    path('regist_page/',regist_page,name='zcjm'),
    path('regist/',regist,name='zc'),
    path('login_page/',login_page,name='dljm'),
    path('login/',login,name='dl'),
    path('yzm/',yzm,name='yzm'),
    path('username_yz',username_yz,name='yz'),
    path('yzm_yz',pd_yzm,name='yzm_pd')

]

