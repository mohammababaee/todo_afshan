
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
# Create your views here.


class TaskAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        return Response(tasks)

    def post(self, request):
        task_serializer = TaskSerializer(data=request.data)
        task_serializer.save()
        return Response({"new Task Added"})
