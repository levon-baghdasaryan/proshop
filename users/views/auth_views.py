from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from ..serializers import UserSerializerWithToken

User = get_user_model()


@api_view(['POST'])
def register(request):
    data = request.data

    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
