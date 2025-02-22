# Generated by Django 5.1.2 on 2024-11-03 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serv_Booking', '0006_alter_userbooking_time_slot'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services', models.CharField(max_length=255)),
                ('car_model', models.CharField(max_length=255)),
                ('car_number', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('timslot', models.CharField(max_length=255)),
                ('payment_status', models.CharField(default='Pending', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Serv_Booking.user_details')),
            ],
        ),
        migrations.DeleteModel(
            name='services_cart',
        ),
    ]
