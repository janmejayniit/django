from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, upload_to='avatar/')

    # USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']