from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
def registerUser(request):

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def getUsers(request):
    if request.method == 'POST':
        user = User.objects.get(user_id=request.data['user_id'])
        if user:
            if request.data['password'] == user.password:
                serializer = UserSerializer(user, many=False)
                return Response(
                    {
                        "message": "Login Successful",
                        "data": serializer.data,
                        "access_token" : "jsdfisidfnsidfbsidfn"
                    },
                    status=status.HTTP_200_OK
                )

        return Response({"message" : "login fail"}
                        , status=status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
def updateUser(request, user_id):
    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        return Response(
            {"error": "User not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = UserSerializer(
        user,
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "User updated",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['DELETE'])
def deleteUser(request, user_id):
    try:
        if request.method == 'DELETE':
            user = User.objects.get(user_id=user_id)
            user.delete()
            return Response({"message" : "user deleted"},status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
