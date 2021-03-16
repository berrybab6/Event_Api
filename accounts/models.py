from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, gender = None, profile_url=None, reset_link=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("User Must have an email address")
        if not password:
            raise  ValueError("User Must have a Password")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.active = is_active
        user.gender = gender
        user.profile_url = ""
        user.reset_link = reset_link
        user.full_name = full_name
        user.admin = is_admin
        user.staff = is_staff
        user.save(using=self._db)
        return user

    def create_superuser(self, email,full_name=None, password=None):
        user = self.create_user(email, full_name=full_name, password=password, is_staff=True, is_admin=True)
        return user
    def create_staffuser(self, email, full_name=None, password=None):
        user = self.create_user(email, full_name=full_name, password=password, is_staff=True)
        return user
# Create User models here.
class User(AbstractBaseUser):
    email = models.CharField(unique=True, max_length=255, default=False)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=12, null=True)
    profile_url = models.ImageField(default=False, null=True, blank=True)
    reset_link = models.CharField(max_length=255, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)