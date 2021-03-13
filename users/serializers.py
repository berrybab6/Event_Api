# from rest_framework import serializers
# from .models import  UserInfo
# from django.contrib.auth import get_user_model


# class UserInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model
#         fields = [
#             'id',
#             'first_name',
#             'last_name',
#             'username',
#             'email',
#             'password']
#             # 'gender',
#             # 'profile_url',
#             # 'reset_link']
#     def create_user(self, validated_data):
#         return UserInfo.objects.create(**validated_data)
#     # def update_user(self, instance, validated_data):
#     #     instance.first_name = validated_data.get('first_name', instance.first_name)
#     #     instance.lastname = validated_data.get('last_name', instance.last_name)
#     #     instance.id = validated_data.get('id', instance.id)
#     #     instance.username = validated_data.get('username', instance.username)
#     #     instance.email = validated_data.get('email', instance.email)
#     #     instance.password = validated_data.get('password', instance.password)
#     #     instance.save()
#     #     return instance