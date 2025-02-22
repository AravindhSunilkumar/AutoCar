# Generated by Django 5.1.2 on 2024-10-31 05:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serv_Booking', '0002_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='services_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Serv_Booking.services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Serv_Booking.user_details')),
            ],
        ),
    ]
