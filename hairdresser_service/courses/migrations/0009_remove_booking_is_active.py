# Generated by Django 5.1.5 on 2025-02-06 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_rename_booking_active_booking_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_active',
        ),
    ]
