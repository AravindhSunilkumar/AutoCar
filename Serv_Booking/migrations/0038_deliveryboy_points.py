# Generated by Django 5.1.3 on 2024-12-04 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serv_Booking', '0037_alter_productsorders_delivery_boy'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryboy',
            name='points',
            field=models.IntegerField(default=5),
        ),
    ]
