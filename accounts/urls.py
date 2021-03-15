from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', views.UserCreationView.as_view()),
    path('login/', views.LoginUserView.as_view()),
    path('forgotpass/', views.ForgotPasswordView.as_view()),
    path('changepass/<int:pk>/', views.ChangePasswordView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view()),
    path('log/',obtain_auth_token, name="login")

]

