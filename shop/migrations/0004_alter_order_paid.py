# Generated by Django 4.0.5 on 2022-07-05 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_alter_order_complete"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="paid",
            field=models.IntegerField(
                choices=[
                    (-1, "Payment on delivery"),
                    (0, "Awaiting payment"),
                    (1, "Paid"),
                ]
            ),
        ),
    ]
