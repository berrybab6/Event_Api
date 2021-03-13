# from django.shortcuts import render
# from rest_framework.decorators import action
# from django.http import *
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from django.http import HttpResponse,JsonResponse
# from rest_framework.response import Response
# from .models import UserInfo
# from rest_framework.permissions import AllowAny
# from .serializers import UserInfoSerializer
# from django.contrib.auth.hashers import make_password,check_password
# import random
# import string


# #  ''.join(choice(digits) for i in xrange(4))


# from rest_framework import viewsets, status, mixins, generics


# class UserInfoList(generics.GenericAPIView):
#     queryset = UserInfo.objects.all()
#     serializer_class = UserInfoSerializer
#     permission_classes = (AllowAny, )

#     # @action(methods=["POST"], detail=True)
#     def post(self,request,format=None):
#         f_name = request.data['first_name']
#         l_name = request.data['last_name']
#         email = request.data['email']
#         username = request.data['username']
#         password = request.data['password']
#         gender = request.data['gender']
#         profile_url = request.data['profile_url']
#         user = UserInfo(first_name=f_name, last_name=l_name, username=username, email=email, password=password,gender=gender, profile_url=profile_url)
#         user.save()
#         serialize = UserInfoSerializer(user)
#         return JsonResponse({"registered":serialize.data}, status=status.HTTP_201_CREATED)
    
#     # @action(methods=['GET'], detail=False)
#     def get(self, request,format=None):
#         user = UserInfo.objects.all()
#         serialize = UserInfoSerializer(user,many=True)
#         return JsonResponse({"user":serialize.data}, status=status.HTTP_200_OK)

# # Create your views here.
# class UserInfoDetail(generics.GenericAPIView):
#     queryset = UserInfo.objects.all()
#     serializer_class = UserInfoSerializer
#     permission_classes = (AllowAny, )
#     # @action(methods=["POST"], detail=True)
#     # def login(self,request):

#     def get_object(self, pk):
#         try:
#             return UserInfo.objects.get(pk=pk)
#         except UserInfo.DoesNotExist:
#             raise Http404

#     # @action(methods=['POST'], detail=True)
#     def change_password(self, request, pk):
#         return JsonResponse({"user":"user"})
#     def get(self,request,pk):
#         user = self.get_object(pk)
#         serialize = UserInfoSerializer(user)
#         return JsonResponse({"user Detail":serialize.data},status=status.HTTP_200_OK)
#     # @action(methods=['DELETE'], detail=True)
#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         #serializer = UserInfoSerializer(user)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     ###change Password
#     def put(self, request, pk):
#         if request.method == 'PUT':
#             user = self.get_object(pk)
#             # password = user.password
#             f_name = request.data['first_name']
#             l_name = request.data['last_name']
#             if f_name and l_name:
#                 user.first_name = f_name
#                 user.last_name = l_name
#                 user.save()
#                 ser = UserInfoSerializer(user)
#                 return JsonResponse({"Edited User":ser.data})
# class RegisterUser(generics.GenericAPIView):
#     queryset = UserInfo.objects.all()
#     serializer_class = UserInfoSerializer
#     permission_classes = (AllowAny, )
#     # @csrf_token
#     @action(methods=['POST'], detail=True)
#     def post(self,request):
#         # user = UserInfo.objects.all()
#         # user.save(# @action(methods=["POST"], detail=True)
#         f_name = request.data['first_name']
#         l_name = request.data['last_name']
#         email = request.data['email']
#         username = request.data['username']
#         password = request.data['password']
#         gender = request.data['gender']
#         profile_url = request.data['profile_url']
#         hashed_pass = make_password(password)
#         # try:
#         user = UserInfo.objects.create_user(password=hashed_pass, email=email, username=username,first_name=f_name,last_name=l_name)
#         # user = UserInfo(first_name=f_name,
#         #                 last_name=l_name,
#         #                 username=username,
#         #                 email=email,
#         #                 password=hashed_pass)
#         #                 # gender=gender,
#         #                 # profile_url=profile_url)
#         # user.save()
#         token = Token.objects.create(user_id=user.id)
#         serializer = UserInfoSerializer(user)
#         return JsonResponse({"user registered":serializer.data, "token":token.key}, status=status.HTTP_201_CREATED)
#         # except Exception:
#             # return JsonResponse({"success":False})
# class LoginUser(ObtainAuthToken):
#     queryset = UserInfo.objects.all()
#     serializer_class = UserInfoSerializer
#     permission_classes = (AllowAny, )

#     def post(self, request, format=None):
#         email = request.data['email']
#         username = request.data['username']
#         password = request.data['password']

#         if password == "" or username == "" or email == "":
#             return JsonResponse({"error":"Fields cant be empty"})
#         else:
#             user = UserInfo.objects.get(email=email)
#             if user:
#                 check = check_password(password, user.password)
#                 if check and user.email == email and user.username == username:
#                     serialize = UserInfoSerializer(user)
#                     # for user in UserInfo.objects.all():
#                     #     Token.objects.get_or_create(user=user)
#                     userT = UserInfo.objects.create(user=user) # your user must not be empty

#                     token = Token.objects.get_or_create(user=user)

#                     return JsonResponse({
#                         "Logged In User":serialize.data, "token":token.key},
#                                         status=status.HTTP_202_ACCEPTED)
#                 else:
#                     return JsonResponse({"error":"fields Must Match"}, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return JsonResponse({"error":"User Doesnot exist"}, status=status.HTTP_404_NOT_FOUND)
# class ChangePassword(generics.GenericAPIView):
#     queryset = UserInfo.objects.all()
#     serializer_class = UserInfoSerializer
#     permission_classes = (AllowAny, )

#     def put(self, request, pk):
#         user = UserInfo.objects.get(id=pk)
#         password = user.password
#         password1 = request.data['password']
#         new_pass = request.data['new_password']
#         if new_pass and password1 and user:
#             # hashed_pass = check_password(password1)
#             if check_password(password1, password):
#                 user.password = make_password(new_pass)
#                 user.save()
#                 ser = UserInfoSerializer(user)
#                 return JsonResponse({"Edited User":ser.data})
#             else:
#                 return JsonResponse({"error":"incorrect password"})
#         else:
#             return JsonResponse({"error":"Fields cant be empty"})
# class ForgotPassword(generics.GenericAPIView):
#     queryset = UserInfo.objects.all()
#     serializer_class = UserInfoSerializer
#     permission_classes = (AllowAny, )

#     def post(self, request, pk):
#         email = request.data['email']
#         user = UserInfo.objects.get(id=pk)
#         if email and user:
#             if user.email == email:
#                 reset_code = ''.join([random.choice(string.ascii_uppercase + string.digits)for _ in range(6)])
#                 user.reset_link = reset_code
#                 user.save()
#                 return JsonResponse({"reset_code":user.reset_link})
#     def put(self,request,pk,format=None):
#         user = UserInfo.objects.get(id=pk)
#         reset_code = request.data['reset_code']
#         password = request.data['password']
#         message = ''
#         if reset_code and password:
#             if reset_code == user.reset_link:
#                 user.password = password
#                 user.reset_link = ''
#                 user.save()
#                 message = 'Password Changed succesfully'
#             else:
#                 message = 'incorrect reset_code'
#         else:
#             message = 'fields cent be empty'
#         return JsonResponse({"message":message})