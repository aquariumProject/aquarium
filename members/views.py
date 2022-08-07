from django.shortcuts import render
from members.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer
from .models import User

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data 
        return Response({"token": token.key}, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView): # 토큰만 삭제하면 되서 시리얼라이저X
    def get(self, request):
        print("************************************")
        print(request.user)
        print("************************************")
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)