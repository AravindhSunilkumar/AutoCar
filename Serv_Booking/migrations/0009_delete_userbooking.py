# Generated by Django 5.0.2 on 2024-11-10 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Serv_Booking', '0008_rename_timslot_bookingorders_time_slot'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserBooking',
        ),
    ]
