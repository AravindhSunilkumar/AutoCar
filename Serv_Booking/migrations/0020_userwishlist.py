# Generated by Django 5.1.3 on 2024-11-25 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serv_Booking', '0019_alter_userproducts_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Serv_Booking.userproducts')),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Serv_Booking.user_details')),
            ],
        ),
    ]
