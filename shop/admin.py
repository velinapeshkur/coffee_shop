from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from shop.models import Order, ShippingAddress, OrderItem
from django.contrib import messages

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email', 'date_ordered', 'payment', 'user', 'complete']
    list_filter = ['complete', 'user']
    search_fields = ['pk', 'email']
    actions = ['mark_complete', 'show_orders', 'delete_with_data']
    
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('order_list/', self.show_orders, name='show_orders'),
        ]
        return my_urls + urls

    @admin.action(description='Mark selected orders as complete')
    def mark_complete(self, request, queryset):
        for order in queryset:
            if order.payment == 0:
                return messages.warning(request, 'You cannot complete unpaid order')
        queryset.update(complete=True)

    
    @admin.action(description='Show selected orders on a separate page')
    def show_orders(self, request, queryset):
        order_items = {}
        
        for obj in queryset:
            order_pk = obj.pk
            order_items[order_pk] = list(OrderItem.objects.filter(order=order_pk))
            
        context = dict(self.admin_site.each_context(request),
                       order_items = order_items,
                       orders = queryset,
                       is_nav_sidebar_enabled = False,
        )            
        return render(request, 'admin/shop/order/order_list.html', context)
    
    @admin.action(description='Delete selected orders with all data')
    def delete_with_data(self, request, queryset):
        for obj in queryset:
            
            if obj.complete:
                order_pk = obj.pk
                address = obj.address.id
                OrderItem.objects.filter(order=order_pk).delete()
                ShippingAddress.objects.filter(id=address).delete()
                obj.delete()
            else:
                messages.warning(request, 'You cannot delete order that is not complete.')


class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ['order']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
