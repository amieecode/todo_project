# Generated by Django 5.1 on 2024-08-19 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='todo_list',
            new_name='todo_name',
        ),
    ]
