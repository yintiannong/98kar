# Generated by Django 2.0.2 on 2018-10-31 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('note', models.CharField(max_length=100)),
                ('Operation', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 't_dep',
            },
        ),
    ]
