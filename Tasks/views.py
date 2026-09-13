from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from models import Task
from serializers import TaskSerializer

@api_view(['GET'])
def filter_tasks(request, user_id):
    try:
        if request.method == 'GET':
            tasks = Task.objects.get(user_id=user_id)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


