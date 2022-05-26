from datetime import datetime
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    creation_date = models.TimeField(default=datetime.now())
    todo_date = models.DateTimeField()
