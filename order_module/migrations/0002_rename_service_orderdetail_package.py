# Generated by Django 3.2.25 on 2024-07-26 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='service',
            new_name='package',
        ),
    ]
