# Generated by Django 2.2 on 2022-03-21 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='last_update',
            new_name='last_update_time',
        ),
    ]
