from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.http import JsonResponse
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializers
# , authenticate
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.
class UserCreationView(generics.GenericAPIView):
    # @action(methods=['POST'], detail=True)
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (AllowAny, )
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = User(email=email)
        user.set_password(password)
        user.save()
        serial = UserSerializers(user)
        return JsonResponse({"user":serial.data})
    

class LoginUserView(generics.GenericAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (AllowAny, )
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({"message":"user logged in succesfully"})
            else:
                return JsonResponse({"error":"disabled account"})
            #Return a 'disabled account' error message
        else:
            return JsonResponse({"error":"invalid login"})
    # Return 'invalid login' error message.
