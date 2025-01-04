# Generated by Django 5.1.3 on 2024-11-27 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serv_Booking', '0024_user_details_address_user_details_pincode'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.IntegerField()),
                ('payment_status', models.CharField(default='pending', max_length=255)),
                ('order_status', models.CharField(default='pending', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Serv_Booking.products')),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Serv_Booking.user_details')),
            ],
        ),
    ]
