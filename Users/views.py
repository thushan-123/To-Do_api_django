from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from models import User
from serializers import UserSerializer

@api_view(['POST'])
def registerUser(request):

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

