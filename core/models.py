from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True,unique=True)
    