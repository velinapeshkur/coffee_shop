from django.contrib import admin
from django.utils import timezone

from coupons.models import Coupon
from coupons.tasks import activate_coupon_task, deactivate_coupon_task


class CouponAdmin(admin.ModelAdmin):
    list_display = ["code", "valid_from", "valid_to", "discount", "active"]
    list_filter = ["active", "valid_from", "valid_to"]
    search_fields = ["code"]

    def save_model(self, request, obj, form, change):
        """
        When coupon is added, schedules Celery task to activate or deactivate
        coupon at specified datetime.
        """
        if obj.valid_from > timezone.now():
            activate_coupon_task.apply_async(args=[obj.id], eta=obj.valid_from)
            obj.active = False
        if obj.valid_to:
            deactivate_coupon_task.apply_async(args=[obj.id], eta=obj.valid_to)
        obj.save()


admin.site.register(Coupon, CouponAdmin)
