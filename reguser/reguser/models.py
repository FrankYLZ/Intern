from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings

class Userreg(models.Model):
    username = models.CharField(max_length = 100, unique=True) 
    email = models.CharField(max_length = 100) 
    password = models.CharField(max_length = 100) 
    gender = models.CharField(max_length = 100) 
    class Meta:
        db_table = "user_signup"
