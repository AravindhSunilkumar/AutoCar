# Generated by Django 5.1.3 on 2024-12-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serv_Booking', '0052_alter_productsorders_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsorders',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
