# Generated by Django 4.1.4 on 2022-12-08 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_order_customer_order_email_order_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('Payment on delivery', 'Delivery Payment'), ('Awaiting payment', 'Awaiting Payment'), ('Paid', 'Paid')], max_length=20),
        ),
    ]
