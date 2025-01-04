# Generated by Django 5.1.3 on 2024-12-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serv_Booking', '0032_alter_deliveryboy_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryboy',
            name='license_number',
        ),
        migrations.RemoveField(
            model_name='deliveryboy',
            name='vehicle_number',
        ),
        migrations.AlterField(
            model_name='deliveryboy',
            name='status',
            field=models.CharField(default='not approved', max_length=255),
        ),
    ]
