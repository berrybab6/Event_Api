from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserCreationView.as_view()),
    path('login/', views.LoginUserView.as_view())
]

