from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Account(AbstractBaseUser):
    avatar = models.ImageField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True)
    # last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')
    REQUIRED_FIELDS = ["email", "password"]
    USERNAME_FIELD = 'email'
# ALTER TABLE 'account_account' ADD last_login DATETIME;