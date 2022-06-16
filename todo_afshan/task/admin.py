from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'todo_date']
    sortable_by = ['todo_date', 'title']
    list_editable = ['todo_date']
    search_fields = ['title']