from django.urls import path
from test_app import views
urlpatterns = [
    path('test_page/',views.test_page,name='test_page'),
    path('test_app/',views.test1,name='test1'),
]