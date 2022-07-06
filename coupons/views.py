from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Coupon
from .forms import CouponApplyForm
from django.contrib import messages

# Create your views here.

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['coupon_id'] = coupon.id
            request.session['coupon_code'] = coupon.code
            request.session['coupon_discount'] = coupon.discount
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
            messages.error(request, "Sorry, this promocode doesn't exist")
        return redirect('shop:checkout')

def coupon_remove(request):
    request.session['coupon_id'] = None
    return redirect('shop:checkout')
