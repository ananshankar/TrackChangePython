# Generated by Django 5.1.7 on 2025-03-17 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_sprint_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprint',
            name='user',
        ),
    ]
