from django.urls import path
# from rest_framework import routers
# from django.conf.urls import include
from .views import UserInfoList,UserInfoDetail
from . import views

# router = routers.DefaultRouter()
# router.register('users', views.UserInfoViewSet, basename="users")
# router.register('users/<int:pk>/',views.UserInfoViewSet,basename="user")
urlpatterns = [
    # path('', include(router.urls)),
    path('', UserInfoList.as_view()),
    path('<int:pk>/', UserInfoDetail.as_view()),
    path('register/', views.RegisterUser.as_view()),
    path('login/', views.LoginUser.as_view()),
    path('changePassword/<int:pk>/', views.ChangePassword.as_view()),
    path('forgotPassword/<int:pk>/', views.ForgotPassword.as_view())
    #path('forgotPassword',views.forgotPassword,name='forgotPassword')
]
