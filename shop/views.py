from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView

from accounts.forms import CustomAuthForm
from cart.cart import Cart
from coupons.forms import CouponApplyForm
from shop.forms import ContactInfoForm, PaymentMethodForm, ShippingAddressForm
from shop.models import Order, OrderItem
from shop.tasks import send_confirmation_email_task


def checkout(request):
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


def create_order(request):

    if request.method == "POST":
        contact_form = ContactInfoForm(request.POST)
        address_form = ShippingAddressForm(request.POST)
        payment_form = PaymentMethodForm(request.POST)
        cart = Cart(request)

        if (
            contact_form.is_valid()
            and address_form.is_valid()
            and payment_form.is_valid()
        ):
            order = contact_form.save(commit=False)

            # Add user if authenticated
            if request.user.is_authenticated:
                order.user = request.user

            # Address
            address = address_form.save()
            order.address = address

            # Calculate total price
            if "coupon_id" in request.session and request.session["coupon_id"]:
                order.total_price = cart.get_coupon_price()
            else:
                order.total_price = cart.get_total_price()

            # Save payment method
            payment_method = payment_form.cleaned_data.get("payment")
            if payment_method == "Online":
                order.payment = Order.AWAITING_PAYMENT
                order.save()
            else:
                order.payment = Order.DELIVERY_PAYMENT
                order.save()

            # Saving order items
            for item in cart:
                if item["price"] != 0:
                    order_item = OrderItem(
                        item=item["product"],
                        order=order,
                        quantity=item["quantity"],
                        cost=item["total_price"],
                    )
                    order_item.save()

            request.session["coupon_id"] = None
            cart.clear()

            if payment_method == "Online":
                return redirect("shop:payment", pk=order.pk)

            return redirect("shop:confirm_order", pk=order.pk)

    return redirect("access_denied")


# A stub for adding payment system
def payment_view(request, pk):
    return render(request, "shop/payment.html", {"order_pk": pk})


# Marks order as paid
def paid(request, pk):
    order = Order.objects.get(pk=pk)
    order.payment = Order.PAID
    order.save()
    return redirect("shop:confirm_order", pk=pk)


def confirm_order(request, pk):
    order_items = OrderItem.objects.filter(order=pk)
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
