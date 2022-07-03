from datetime import datetime
from django.db import models

from user.models import CustomUser

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField(blank=True)
    creation_date = models.DateTimeField(default=datetime.now())
    todo_date = models.DateTimeField(blank=True, null=True)
    #writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    