# Generated by Django 5.1.3 on 2024-12-03 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Serv_Booking', '0034_productsorders_delivery_boy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsorders',
            name='delivery_boy',
        ),
    ]
