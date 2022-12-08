from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_student = models.BooleanField(default=False)
    name = models.CharField(max_length=25,null=True)
    parent_name = models.CharField(max_length=25,null=True)
    address = models.TextField(null=True)
    mobile_no = models.IntegerField(null=True)
    roll_no = models.IntegerField(null=True)
    admission_no= models.IntegerField(null=True)