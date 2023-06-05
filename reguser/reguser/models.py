from django.db import models
from django.contrib import admin


class Userreg(models.Model):
    username = models.CharField(max_length = 100) 
    email = models.CharField(max_length = 100) 
    password = models.CharField(max_length = 100) 
    gender = models.CharField(max_length = 100) 
    class Meta:
        db_table = "user_signup"