from django.db import models

# Create your models here.
class Admin(models.Model):
   username=models.CharField(max_length=30,null=True)
   name=models.CharField(max_length=10,null=True)
   password=models.CharField(max_length=10,null=True)
   sex=models.SmallIntegerField(null=True)
   birth=models.DateField(null=True)
   class Meta:
       db_table='admin_t'