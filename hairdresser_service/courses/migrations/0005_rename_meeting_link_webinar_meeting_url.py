# Generated by Django 5.1.5 on 2025-02-05 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_webinar_meeting_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webinar',
            old_name='meeting_link',
            new_name='meeting_url',
        ),
    ]
