from django.contrib import messages
from django.http import HttpRequest
from django.utils import timezone

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


def save_coupon_in_session(request: HttpRequest, code: str) -> None:
    """
    Saves coupon data in session or diaplays error message,
    if coupon doesn't exist.
    """
    now = timezone.now()
    try:
        coupon = Coupon.objects.get(
            code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True
        )
        request.session["coupon_id"] = coupon.pk
        request.session["coupon_code"] = coupon.code
        request.session["coupon_discount"] = coupon.discount
    except Coupon.DoesNotExist:
        request.session["coupon_id"] = None
        messages.error(request, "Sorry, this promocode doesn't exist")
