from django.contrib import admin
from shop.models import Order, ShippingAddress, OrderItem

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
