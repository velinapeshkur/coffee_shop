from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from cart.cart import Cart
from shop.models import Order, OrderItem


def send_confirmation_email(order_pk: int) -> int:
    """
    Sends confirmation email after purchase is made.
    Called by Celery task.
    """
    order = Order.objects.get(pk=order_pk)
    order_items = list(OrderItem.objects.filter(order=order))

    subject = f"Order #{order_pk} Confirmation"
    html_message = render_to_string(
        "shop/email_template.html", {"order": order, "order_items": order_items}
    )
    return send_mail(
        subject=subject,
        message=strip_tags(html_message),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[order.email],
        html_message=html_message,
        fail_silently=False,
    )


def mark_order_as_paid(order_pk: int) -> None:
    """
    Marks order as paid.
    """
    order = Order.objects.get(pk=order_pk)
    order.payment = Order.Payment.PAID
    order.save()


class CreateOrder:
    """
    Receives contact, address and payment forms.
    Creates and saves order to database.
    """

    def __init__(self, contact_form, address_form, payment_form):
        self._contact_form = contact_form
        self._address_form = address_form
        self._payment_form = payment_form

    def create_order(self, request):
        cart = Cart(request)
        order = self._contact_form.save(commit=False)

        self._add_user(request, order)
        self._add_address(order)
        self._calculate_total_price(request, order, cart)
        self._add_payment_method(order)
        self._save_order_items(order, cart)
        self._clear_cart(request, cart)

        return order

    def _add_user(self, request, order):
        if request.user.is_authenticated:
            order.user = request.user

    def _add_address(self, order):
        address = self._address_form.save()
        order.address = address

    def _calculate_total_price(self, request, order, cart):
        if "coupon_id" in request.session and request.session["coupon_id"]:
            order.total_price = cart.get_coupon_price()
        else:
            order.total_price = cart.get_total_price()

    def _add_payment_method(self, order):
        payment_method = self._payment_form.cleaned_data.get("payment")
        if int(payment_method) == 0:
            order.payment = Order.Payment.AWAITING_PAYMENT
            order.save()
        else:
            order.payment = Order.Payment.DELIVERY_PAYMENT
            order.save()

    def _save_order_items(self, order, cart):
        for item in cart:
            if item["price"] != 0:
                order_item = OrderItem(
                    item=item["product"],
                    order=order,
                    quantity=item["quantity"],
                    cost=item["total_price"],
                )
                order_item.save()

    def _clear_cart(self, request, cart):
        request.session["coupon_id"] = None
        cart.clear()
