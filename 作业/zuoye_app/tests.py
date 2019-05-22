import os

import django
from django.test import TestCase

# Create your tests here.


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "作业.settings")
django.setup()
from zuoye_app.models import employee, Category, Student, Course, User


#一对多查询：
def otoo():
    # user=employee.objects.get(id=1)
    #
    # op=user.rele.create_time #get后得到一条数据，得到的是一个Category对象，直接点便可获得给对象中的信息
    # print(op)

    # user=employee.objects.filter(id=2)
    # op=user[0].rele.create_time#filter以后得到多条数据，是个列表
    # print(op)

    user=Category.objects.get(id=2)   #查询部门
    op=user.employee_set.filter()
    print(op)




#多对多：

def mtom():
    # student=Student.objects.get(id=1)
    # op=student.course_set.filter()
    #
    # print(op)


    course=Course.objects.get(id=2)
    op=course.rel.filter()
    print(op)


#一对一
def otoi():
    person=User.objects.get(id=1)
    a=person.number.note#获得一个numer对象
    print(a)

if __name__ == '__main__':
    otoi()