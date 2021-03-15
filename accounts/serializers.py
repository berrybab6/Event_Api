from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'gender', 'profile_url', 'full_name', 'reset_link']

