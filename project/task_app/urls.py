from django.urls import path

from task_app.views import emplist_page, user_add_page, user_add, delete, update_page, update1

urlpatterns = [
    path('emplist/',emplist_page,name='syjm'),
    path('add_page',user_add_page,name='add_page'),
    path('add',user_add,name='tj'),
    path('del/',delete,name='sc'),
    path('update_page/',update_page,name='gx'),
    path('update1/',update1,name='gxcg')
]
