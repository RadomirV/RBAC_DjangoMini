<<<<<<< HEAD
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


    

class CustomUser(AbstractUser):
    ROLES = [
        ('user', 'User'),
        ('admin', 'Admin'),
        ('moderator','Moderator')
    ]
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    objects = CustomUserManager()
    
    
    
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
=======
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)



class CustomUser(AbstractUser):
    ROLES = [
        ('user', 'User'),
        ('admin', 'Admin'),
        ('moderator','Moderator')
    ]
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    objects = CustomUserManager()
>>>>>>> 84cd1563f84fde80347479da1b81d5b66bc77fea
