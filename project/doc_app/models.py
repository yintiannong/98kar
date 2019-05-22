from django.db import models

# Create your models here.
class Dept(models.Model):
    name=models.CharField(max_length=10,unique=True)
    note=models.CharField(max_length=100)
    Operation=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='t_dep'

