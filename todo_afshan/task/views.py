
from asyncio import tasks
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from yaml import serialize
from .models import Task
from .serializers import TaskSerializer
from task import serializers
# Create your views here.


@api_view(['GET'])
def TaskList(resquest):
    tasks = Task.objects.all()
    serializers = TaskSerializer(tasks, many=True)
    return Response(serializers.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
