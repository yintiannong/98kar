from django.db import models
from doc_app.models import Dept

# Create your models here.
class task(models.Model):
    name=models.CharField(max_length=10,null=True)
    salary=models.IntegerField(null=True)
    age=models.IntegerField(null=True)
    gender=models.SmallIntegerField(null=True)
    birth=models.DateField(null=True)
    pic1=models.ImageField(upload_to='user',null=True,default='user/wupingguo.jpg')
    dept=models.ForeignKey(to=Dept,on_delete=models.CASCADE,null=True)
    class Meta():
        db_table='employee'


