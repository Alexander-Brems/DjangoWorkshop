# Generated by Django 2.2.4 on 2019-11-05 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='notes',
            new_name='text',
        ),
    ]
