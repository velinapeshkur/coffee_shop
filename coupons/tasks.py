from __future__ import absolute_import, unicode_literals

from celery import shared_task

from coupons import services


@shared_task
def activate_coupon_task(coupon_id):
    return services.activate_coupon(coupon_id)


@shared_task
def deactivate_coupon_task(coupon_id):
    return services.deactivate_coupon(coupon_id)
