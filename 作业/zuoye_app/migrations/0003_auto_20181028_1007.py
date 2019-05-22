# Generated by Django 2.0.2 on 2018-10-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zuoye_app', '0002_auto_20181028_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('birth', models.DateTimeField()),
            ],
            options={
                'db_table': 't_student',
            },
        ),
        migrations.RemoveField(
            model_name='employee',
            name='rele',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='employee',
        ),
    ]
