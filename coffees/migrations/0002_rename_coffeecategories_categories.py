# Generated by Django 4.0.5 on 2022-06-16 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("coffees", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CoffeeCategories",
            new_name="Categories",
        ),
    ]
