# Generated by Django 3.2.25 on 2024-07-14 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0005_alter_sitesetting_phone_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='instagram_link',
            field=models.CharField(max_length=100, verbose_name=' لینک اینستاگرام'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='telegram_link',
            field=models.CharField(max_length=100, verbose_name=' لینک تلگرام'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='whatsapp_link',
            field=models.CharField(max_length=100, verbose_name='لینک واتس آپ'),
        ),
    ]
