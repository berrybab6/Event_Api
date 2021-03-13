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
    # permission_classes = (AllowAny, )
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        # user = authenticate(email=email, password=password)
        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        #         return JsonResponse({"message":"user logged in succesfully"})
        #     else:
        #         return JsonResponse({"error":"disabled account"})
        #     #Return a 'disabled account' error message
        # else:
        #     return JsonResponse({"error":"invalid login"})
        # Return an 'invalid login' error message.
        user = User(email=email)
        user.set_password(password)
        user.save()
        serial = UserSerializers(user)
        return JsonResponse({"user":serial.data})
    

# Function based views to Class Based Views

# def login_view(request, *args, **kwargs):
#     form = AuthenticationForm(request, data=request.POST or None)
#     if form.is_valid():
#         user_ = form.get_user()
#         login(request, user_)
#         return redirect("/")
#     context = {
#         "form": form,
#         "btn_label": "Login",
#         "title": "Login"
#     }
#     return render(request, "accounts/auth.html", context)

# def logout_view(request, *args, **kwargs):
#     if request.method == "POST":
#         logout(request)
#         return redirect("/login")
#     context = {
#         "form": None,
#         "description": "Are you sure you want to logout?",
#         "btn_label": "Click to Confirm",
#         "title": "Logout"
#     }
#     return render(request, "accounts/auth.html", context)


# def register_view(request, *args, **kwargs):
#     form = UserCreationForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=True)
#         user.set_password(form.cleaned_data.get("password1"))
#         # send a confirmation email to verify their account
#         login(request, user)
#         return redirect("/")
#     context = {
#         "form": form,
#         "btn_label": "Register",
#         "title": "Register"
#     }
#     return render(request, "accounts/auth.html", context)