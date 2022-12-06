from django.db import models

# Create your models here.

# user model

class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=200)
    FullName = models.CharField(max_length=200)
   
    IsSuperUser = models.CharField(max_length=100)
    Department = models.CharField(max_length=200)
    Designation = models.CharField(max_length=200)
    Password = models.CharField(max_length=255)
    