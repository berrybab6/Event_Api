# #from django.db import models
# # from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.conf import settings
# from rest_framework.authtoken.models import Token
# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# #from django.contrib.auth.models import User
# class UserInfoManager(BaseUserManager):
#     use_in_migrations = True
#     def _create_user(self, email, password, username, first_name, last_name):
#         if not email or not password or not username or not first_name or not last_name:
#             raise ValueError('Fields Cant be empty')

#         user = self.model(
#             email=email,
#             last_name=last_name,
#             username=username,#.normalize_username(username),
#             first_name=first_name
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, username, last_name, first_name, password):
#         user = self._create_user(email, last_name=last_name, first_name=first_name, username=username, password=password)
#         user.save(using=self._db)
#         return user

# # Create your models here.
# class UserInfo(AbstractBaseUser):
#     objects = UserInfoManager()
#     #user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=100, null=True)
#     last_name = models.CharField(max_length=100, null=True)
#     username = models.CharField(max_length=100, unique=True, default=False)
#     email = models.CharField(max_length=120, null=True)
#     password = models.CharField(max_length=255, null=True)
#     gender = models.CharField(max_length=12, null=True)
#     profile_url = models.URLField()
#     reset_link = models.CharField(max_length=255, null=True)
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []
#     class Meta:
#         ordering = []

# # create token class
# class Token(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# @receiver(post_save, sender=UserInfo)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
