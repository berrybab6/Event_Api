from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from rest_framework.decorators import action
from .models import User
from django.contrib.auth.hashers import make_password,check_password

from .serializers import UserSerializers
from rest_framework.authtoken.views import ObtainAuthToken

# , authenticate
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
# from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.
import random
import string
from rest_framework.authtoken.models import Token

class UserCreationView(generics.GenericAPIView):
    # @action(methods=['POST'], detail=True)
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (AllowAny, )
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        gender = request.data.get('gender', "")
        profile_url = request.data.get('profile_url', "")
        full_name = request.data.get('full_name', "")
        user = User(email=email, profile_url=profile_url, gender=gender, full_name=full_name)
        user.set_password(password)
        user.save()
        # token = Token.objects.get(user=user).key
        serial = UserSerializers(user)
        return JsonResponse({"user":serial.data})
    
    def get(self, request,format=None):
        user = User.objects.all()
        serialize = UserSerializers(user,many=True)
        return JsonResponse(serialize.data,safe=False, status=status.HTTP_200_OK)
    

class LoginUserView(ObtainAuthToken):
    
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
                token, created = Token.objects.get_or_create(user=user)

                ser = UserSerializers(user)
                return JsonResponse({"message":"user logged in succesfully", "user":ser.data, "token":token.key})
            else:
                return JsonResponse({"error":"disabled account"})
            #Return a 'disabled account' error message
        else:
            return JsonResponse({"error":"invalid login"})
    # Return 'invalid login' error message.
class UserDetailView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (AllowAny, )
    def get(self,request,pk):
        user = User.objects.get(id=pk)
        serialize = UserSerializers(user)
        return JsonResponse({"user Detail":serialize.data},status=status.HTTP_200_OK)
    # @action(methods=['DELETE'], detail=True)
    def delete(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        #serializer = UserInfoSerializer(user)
        user.delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
    ###change Password
class ForgotPasswordView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (AllowAny, )

    def post(self, request):
        email = request.data['email']
        user = User.objects.get(email=email)
        if email and user:
            if user.email == email:
                reset_code = ''.join([random.choice(string.ascii_uppercase + string.digits)for _ in range(6)])
                user.reset_link = reset_code
                user.save()
                return JsonResponse({"reset_code":user.reset_link})
    def put(self,request, format=None):
        message = ''
        reset_code = request.data['reset_link']
        password = request.data['password']
        if reset_code and password:
            user = User.objects.get(reset_link=reset_code)
            if user:
                # ser = UserSerializers(user)
                user.set_password(password)
                user.reset_link = ''
                user.save()
                ser = UserSerializers(user)
                message = 'Password Changed succesfully'
            else:
                message = 'incorrect reset_code'
        else:
            message = 'fields cent be empty'
        return JsonResponse({"message":message, "user":ser.data})


class ChangePasswordView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (AllowAny, )

    def put(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        password = user.password
        password1 = request.data['password']
        new_pass = request.data['new_password']
        if new_pass and password1 and user:
            # hashed_pass = check_password(password1)
            if check_password(password1, password):
                user.set_password(new_pass)
                user.save()
                ser = UserSerializers(user)
                return JsonResponse({"Edited User":ser.data})
            else:
                return JsonResponse({"error":"incorrect password"})
        else:
            return JsonResponse({"error":"Fields cant be empty"})