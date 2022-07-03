from django.urls import path
from . import views


urlpatterns = [
    path('ping/', views.ping, name='ping'),
    path('task-list/', views.taskList, name='task-list'),
    path('create-task/', views.taskCreate, name='create-task'),
    path('detail-task/<str:pk>/', views.taskDetail, name='detail-task'),
    path('delete-task/<str:pk>/', views.taskDelete, name='delete-task'),
]
