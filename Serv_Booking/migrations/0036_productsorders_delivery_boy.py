# Generated by Django 5.1.3 on 2024-12-03 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serv_Booking', '0035_remove_productsorders_delivery_boy'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsorders',
            name='delivery_boy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Serv_Booking.deliveryboy'),
            preserve_default=False,
        ),
    ]
