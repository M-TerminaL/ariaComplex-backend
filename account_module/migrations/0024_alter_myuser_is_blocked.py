# Generated by Django 3.2.25 on 2024-08-07 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0023_auto_20240806_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_blocked',
            field=models.BooleanField(default=False, verbose_name='مسدود شده / نشده'),
        ),
    ]
