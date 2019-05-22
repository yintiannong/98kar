from django.urls import path

from application_app.views import show, addemp_page, addemp_page_onclik, dele, update, update_r

urlpatterns=[
    path('emplist/',show,name='show1'),
    path('addemp/',addemp_page,name='add1'),
    path('addemp_page_onclik',addemp_page_onclik,name='succ'),
    path('dele/',dele,name='delete'),
    path('update/',update,name='up'),
    path('update_r',update_r,name='update_r')
]