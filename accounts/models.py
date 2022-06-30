from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User as auth_User
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(auth_User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    
    def get_absolute_url(self):
        return reverse('accounts:update',  kwargs={'pk': self.pk})  

    def __str__(self):
        return f'{self.username}'
    
