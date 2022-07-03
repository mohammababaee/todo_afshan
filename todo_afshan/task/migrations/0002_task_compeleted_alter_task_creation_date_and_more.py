# Generated by Django 4.0.2 on 2022-07-03 06:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='compeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 6, 38, 16, 927545)),
        ),
        migrations.AlterField(
            model_name='task',
            name='todo_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
