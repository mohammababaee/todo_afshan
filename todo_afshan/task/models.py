from datetime import datetime
from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField(blank=True)
    creation_date = models.DateTimeField(default=datetime.now())
    todo_date = models.DateTimeField(blank=False,null=False)
    