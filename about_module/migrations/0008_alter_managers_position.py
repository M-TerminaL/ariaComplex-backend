# Generated by Django 3.2.25 on 2024-08-09 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_module', '0007_alter_managers_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managers',
            name='position',
            field=models.CharField(max_length=30, verbose_name='سمت'),
        ),
    ]
