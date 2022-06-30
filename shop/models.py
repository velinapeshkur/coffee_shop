from multiprocessing import cpu_count
from django.db import models
from accounts.models import Customer
from coffees.models import Coffee
from django_countries.fields import CountryField


# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField()
    transaction_id = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.transaction_id)

class ShippingAddress(models.Model):
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    country = CountryField()
    state = models.CharField(max_length=256)
    postal_code = models.IntegerField()

    def __str__(self):
        return str(self.address)


class OrderItem(models.Model):
    item = models.ForeignKey(Coffee, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
