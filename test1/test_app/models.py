from django.db import models

# Create your models here.
class Table(models.Model):
    username=models.CharField(max_length=30)
    name=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
    sex=models.BooleanField()
    birth=models.DateTimeField()
    class Meta:
        db_table='admin_t'