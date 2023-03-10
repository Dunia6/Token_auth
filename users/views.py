from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .sirializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# Create your views here.

class UserDetailAPI(APIView):
    """ To get User Detail using Token Autehtication """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny)
    
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class RegisterUserAPIView(generics.CreateAPIView):
    """ View class to register user """
    permission_classes = (AllowAny)
    serializer_class = RegisterSerializer

