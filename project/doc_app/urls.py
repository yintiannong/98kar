from django.urls import path
#
# from task_app.views import emplist_page, user_add_page, user_add, delete, update_page, update1
from doc_app.views import dept_page, dept_add_page, dept_add, xq, update_page, update, d_dep_page, d_dep

urlpatterns = [

  path('dep_page/',dept_page,name='bmjm'),
  path('add_dept_page/',dept_add_page,name='dtjym'),
  path('add_dept/',dept_add,name='dtj'),
  path('xq/',xq,name='xq'),
  path('update_page',update_page,name='dgxjm'),
  path('update',update,name='dgx'),
  path('add_d_e/',d_dep_page,name='tjyg'),
  path('save/',d_dep,name='save')
]
