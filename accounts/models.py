from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User as auth_User
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class User(auth_User,PermissionsMixin):  
    
    def get_absolute_url(self):
        return reverse('accounts:update',  kwargs={'pk': self.pk})  

    def __str__(self):
        return f'{self.username}'
