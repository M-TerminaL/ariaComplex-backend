# Generated by Django 3.2.25 on 2024-07-24 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_module', '0007_alter_services_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2024, 7, 24), verbose_name='تاریخ ایجاد'),
            preserve_default=False,
        ),
    ]
