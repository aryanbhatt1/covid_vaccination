# Generated by Django 4.0.6 on 2022-07-06 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccinationCentre', '0007_alter_bookings_timedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='timeDate',
        ),
    ]
