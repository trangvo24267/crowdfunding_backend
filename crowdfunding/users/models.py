from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    def __str__(self): #TYPE<OBJ><CUSTOM>
        return self.username

