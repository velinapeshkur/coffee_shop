from django.db import models
from django.urls import reverse

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category_name


class Coffee(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    altitude = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    notes = models.CharField(max_length=50)
    price = models.FloatField() 
    amount = models.IntegerField(default=0)
    description = models.CharField(max_length=3000)
    image = models.ImageField(null=True, upload_to='coffees')

    def out_of_stock(self):
        return self.amount == 0

    def __str__(self):
        return self.name
