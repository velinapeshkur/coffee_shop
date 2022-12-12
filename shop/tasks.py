from __future__ import absolute_import, unicode_literals

from celery import shared_task

from shop import services


@shared_task
def send_confirmation_email_task(order_pk):
    return services.send_confirmation_email(order_pk)
