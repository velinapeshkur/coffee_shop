from shop.models import OrderItem, Order
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_confirmation_email(order_pk: int) -> int:
    """
    Sends confirmation email after purchase is made.
    Called by Celery task.
    """
    order = Order.objects.get(pk=order_pk)
    order_items = list(OrderItem.objects.filter(order=order))
    
    subject = f'Order #{order_pk} Confirmation'
    html_message = render_to_string(
        'shop/email_template.html',
        {'order': order,'order_items': order_items}
        )
    return send_mail(
        subject=subject, 
        message=strip_tags(html_message),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[order.email], 
        html_message=html_message, 
        fail_silently=False
        )
