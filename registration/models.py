from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Stu_Reg(AbstractBaseUser):
    username=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    city=models.CharField(max_length=30)

class Meta:
    db_table="student"


# Create your models here.
