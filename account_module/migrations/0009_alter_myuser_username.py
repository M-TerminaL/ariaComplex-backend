# Generated by Django 3.2.25 on 2024-07-24 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0008_alter_myuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=200, unique=True, verbose_name='شماره موبایل ادمین'),
        ),
    ]
