from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView

from accounts.forms import CustomAuthForm
from cart.cart import Cart
from coupons.forms import CouponApplyForm
from shop import services
from shop.forms import ContactInfoForm, PaymentMethodForm, ShippingAddressForm
from shop.models import Order, OrderItem
from shop.tasks import send_confirmation_email_task


def checkout_view(request):
    cart = Cart(request)

    if len(cart) == 0:
        return redirect("access_denied")

    contact_form = ContactInfoForm
    address_form = ShippingAddressForm
    payment_form = PaymentMethodForm
    login_form = CustomAuthForm
    coupon_form = CouponApplyForm

    return render(
        request,
        "shop/checkout.html",
        context={
            "cart": cart,
            "contact_form": contact_form,
            "address_form": address_form,
            "payment_form": payment_form,
            "login_form": login_form,
            "coupon_form": coupon_form,
        },
    )


def create_order_view(request):

    if request.method == "POST":
        contact_form = ContactInfoForm(request.POST)
        address_form = ShippingAddressForm(request.POST)
        payment_form = PaymentMethodForm(request.POST)

        if (
            contact_form.is_valid()
            and address_form.is_valid()
            and payment_form.is_valid()
        ):
            order = services.CreateOrder(
                contact_form, address_form, payment_form
            ).create_order(request)

            payment_method = payment_form.cleaned_data.get("payment")

            if int(payment_method) == 0:
                return redirect("shop:payment", pk=order.pk)

            return redirect("shop:confirm_order", pk=order.pk)

    return redirect("access_denied")


# A stub for adding payment system
def payment_view(request, pk):
    return render(request, "shop/payment.html", {"order_pk": pk})


def mark_order_as_paid_view(request, pk):
    services.mark_order_as_paid(order_pk=pk)
    return redirect("shop:confirm_order", pk=pk)


def confirm_order_view(request, pk):
    order_items = OrderItem.objects.filter(order=pk).select_related("item")
    for item in order_items:
        item.item.amount -= item.quantity
        item.item.save()
    send_confirmation_email_task.delay(order_pk=pk)
    return render(
        request,
        "shop/order_confirmation.html",
        context={"order_pk": pk, "order_items": order_items},
    )


class OrderListView(ListView, LoginRequiredMixin):
    model = Order
    template_name = "shop/order_history.html"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by(
            "complete", "-date_ordered"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = list(Order.objects.filter(user=self.request.user))
        order_items = {}
        for order in orders:
            order_items[order.pk] = list(OrderItem.objects.filter(order=order.pk))
        context["order_items"] = order_items
        return context
