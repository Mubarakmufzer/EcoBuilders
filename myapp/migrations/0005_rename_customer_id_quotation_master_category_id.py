# Generated by Django 3.2.12 on 2022-02-21 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_category_master_customer_details_designation_master_messages_quotation_details_quotation_master_quot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotation_master',
            old_name='customer_id',
            new_name='category_id',
        ),
    ]
