from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from coupons import services
from coupons.forms import CouponApplyForm


@require_POST
def coupon_apply_view(request):
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data["code"]
        services.save_coupon_in_session(request, code)
        return redirect("shop:checkout")


def coupon_remove_view(request):
    request.session["coupon_id"] = None
    return redirect("shop:checkout")
