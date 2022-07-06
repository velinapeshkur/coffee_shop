from django.contrib import admin
from coffees.models import Coffee, Categories

# Register your models here.

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'category']
    list_filter = ['category']
    list_editable = ['amount']
    search_fields = ['name']
    
admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Categories)
