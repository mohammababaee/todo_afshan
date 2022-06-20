from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)
    description = serializers.TextField()
    creation_date = serializers.DateTimeField()
    todo_date = serializers.DateTimeField()

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        return task
