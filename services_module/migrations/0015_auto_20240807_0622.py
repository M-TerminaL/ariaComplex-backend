# Generated by Django 3.2.25 on 2024-08-07 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services_module', '0014_auto_20240807_0615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='keyword_eight',
        ),
        migrations.RemoveField(
            model_name='services',
            name='keyword_nine',
        ),
        migrations.RemoveField(
            model_name='services',
            name='keyword_ten',
        ),
    ]
