# Generated by Django 5.1.7 on 2025-03-23 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_userprojectrelation_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sprint',
            old_name='sprint_name',
            new_name='label',
        ),
    ]
