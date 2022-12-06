from django.contrib.auth.models import User as auth_User
from django.db import models
from django_countries.fields import CountryField

from coffees.models import Coffee

# Create your models here.


class ShippingAddress(models.Model):
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    country = CountryField()
    state = models.CharField(max_length=256)
    postal_code = models.IntegerField()

    def __str__(self):
        return str(self.address)


class Order(models.Model):
    DELIVERY_PAYMENT = -1
    AWAITING_PAYMENT = 0
    PAID = 1

    PAYMENT_OPTIONS = (
        (DELIVERY_PAYMENT, "Payment on delivery"),
        (AWAITING_PAYMENT, "Awaiting payment"),
        (PAID, "Paid"),
    )

    user = models.ForeignKey(
        auth_User, on_delete=models.SET_NULL, null=True, blank=True
    )
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.ForeignKey(
        ShippingAddress, to_field="id", on_delete=models.SET_NULL, null=True
    )
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(null=True)
    payment = models.IntegerField(choices=PAYMENT_OPTIONS)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200)

    def __str__(self):
        return str(self.pk)


class OrderItem(models.Model):
    item = models.ForeignKey(Coffee, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    cost = models.FloatField(null=True)

    def __str__(self):
        return f"order {self.order}"
