from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from App.users.managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True, primary_key=True)

    first_name = models.CharField(max_length = 255, null=True)
    last_name= models.CharField(max_length = 255, null=True)
    address = models.CharField(max_length = 255, null=True)
    organization_name = models.CharField(max_length = 255, null=True)
    contact_info = models.CharField(max_length = 255, null=True)

    user_class = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return '{}-{}'.format(self.username, self.email)