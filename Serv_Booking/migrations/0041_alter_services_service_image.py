# Generated by Django 5.1.3 on 2024-12-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serv_Booking', '0040_alter_products_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='service_image',
            field=models.FileField(blank=True, null=True, upload_to='services_images/'),
        ),
    ]
