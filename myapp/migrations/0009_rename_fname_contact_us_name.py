# Generated by Django 3.2.13 on 2022-05-08 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_contact_us'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_us',
            old_name='fname',
            new_name='name',
        ),
    ]
