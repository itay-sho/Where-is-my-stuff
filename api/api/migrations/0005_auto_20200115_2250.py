# Generated by Django 3.0.2 on 2020-01-15 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200115_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='current_user',
            new_name='current_person',
        ),
    ]