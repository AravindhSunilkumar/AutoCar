# Generated by Django 5.1.3 on 2024-11-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serv_Booking', '0026_productsorders_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='user_image',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productsorders',
            name='order_status',
            field=models.CharField(default='ordered', max_length=255),
        ),
    ]
