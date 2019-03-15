from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager

class CustomUserManager(UserManager):
    pass

# Create your models here.
class CustomUser(AbstractUser):
	email=models.EmailField(unique=True)
	
	USERNAME_FIELD='email'
	REQUIRED_FIELDS=['username']

	object=CustomUserManager()
  
	def __str__(self):
  		return self.username