# Generated by Django 2.0.2 on 2018-10-30 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='task',
            name='pic1',
            field=models.ImageField(null=True, upload_to='user'),
        ),
    ]