from django.apps import apps
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone


class UserProfileManager(BaseUserManager):

    def create_user(self, email, username, password=None, **kwargs):
        if not email:
            raise ValueError('You must enter an email address')
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **kwargs):
        user = self.create_user(email, username, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Gender(models.TextChoices):
    ذكر = 'ذكر', 'ذكر'
    انثى = 'انثى', 'انثى'


class UserProfile(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(
        max_length=255, unique=True, validators=[username_validator])
    phone = models.CharField(max_length=50, unique=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    join_date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(
        max_length=255, blank=True, null=True, choices=Gender.choices)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username
