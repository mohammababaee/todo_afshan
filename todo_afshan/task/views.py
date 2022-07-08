
from asyncio import tasks
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from yaml import serialize
from .models import Task
from .serializers import TaskSerializer
from task import serializers
from rest_framework.permissions import IsAuthenticated
# Create your views here.

permission_classes = (IsAuthenticated, )


@api_view(['GET'])
def taskList(resquest):
    tasks = Task.objects.all()
    serializers = TaskSerializer(tasks, many=True)
    return Response(serializers.data, status=200)


@api_view(['GET'])
def ping(resquest):
    return Response(status=200)


@api_view(['GET'])
def taskDetail(resquest, pk):
    tasks = Task.objects.get(id=pk)
    serializers = TaskSerializer(tasks, many=False)
    return Response(serializers.data, status=200)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=201)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task deleted !", status=200)


@api_view(['PUT'])
def taskEdit(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data,partial=False)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)