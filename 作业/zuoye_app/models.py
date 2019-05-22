from django.db import models

# Create your models here.
class Category(models.Model):
    ctitle = models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='t_category'

class employee(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    birth=models.DateTimeField()
    rele=models.ForeignKey(to=Category,on_delete=models.CASCADE,db_column='cate_id')
    class Meta:
        db_table='t_employee'



class Student(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    birth=models.DateTimeField()
    class Meta:
        db_table='t_student'


class Course(models.Model):
    coursr_name=models.CharField(max_length=10)
    creat_time=models.DateTimeField(auto_now=True)
    rel=models.ManyToManyField(to=Student)
    class Meta:
        db_table='t_course'



class User(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    class Meta:
        db_table='t_user'

class Number(models.Model):
    user_id=models.IntegerField(unique=True)
    note=models.CharField(max_length=20)
    rel=models.OneToOneField(to=User,on_delete=models.CASCADE)
    class Meta:
        db_table='t_number'

