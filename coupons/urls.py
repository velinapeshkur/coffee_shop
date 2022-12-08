from django.urls import path

from coupons import views

app_name = "coupons"

urlpatterns = [
    path("apply/", views.coupon_apply_view, name="apply"),
    path("remove/", views.coupon_remove_view, name="remove"),
]
