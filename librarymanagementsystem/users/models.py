from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('User must have a Username')

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(
            username, password=password
        )

        user.is_admin = True
        user.save(using=self._db)

        return user


USER_ROLE = (
    ('librarian', 'Librarian'),
    ('member', 'Member')
)


class User(AbstractBaseUser):
    username = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(
        max_length=25, choices=USER_ROLE, default='members')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        full_name = self.name
        return full_name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.username

    def has_perm(self, perm):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    objects = UserManager()
