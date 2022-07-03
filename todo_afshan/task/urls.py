from django.urls import path
from . import views


urlpatterns = [
    path('task-list/', views.TaskList, name='task-list'),
    path('create-task/', views.taskCreate, name='create-task'),
]
