from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    def get_absolute_url(self):
        return reverse("accounts:update", kwargs={"pk": self.pk})
