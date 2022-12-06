from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User as auth_User
from django.urls import reverse

# Create your models here.


class CustomUser(auth_User, PermissionsMixin):
    def get_absolute_url(self):
        return reverse("accounts:update", kwargs={"pk": self.pk})
