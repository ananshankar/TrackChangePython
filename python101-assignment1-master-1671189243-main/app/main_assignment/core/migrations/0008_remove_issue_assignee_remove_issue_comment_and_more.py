# Generated by Django 5.1.7 on 2025-03-23 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_sprint_end_date_alter_sprint_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='label',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='watcher',
        ),
    ]
