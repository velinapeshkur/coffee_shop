from coupons.models import Coupon


def activate_coupon(coupon_id: int) -> None:
    """
    Marks coupon as active. Called by Celery task.
    """
    coupon = Coupon.objects.get(id=coupon_id)
    coupon.active = True
    coupon.save()


def deactivate_coupon(coupon_id: int) -> None:
    """
    Marks coupon as inactive. Called by Celery task.
    """
    coupon = Coupon.objects.get(id=coupon_id)
    coupon.active = False
    coupon.save()
