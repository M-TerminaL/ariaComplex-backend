# Generated by Django 3.2.25 on 2024-08-09 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services_module', '0016_auto_20240807_0643'),
        ('home_module', '0003_alter_homeservices_svc_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeservices',
            name='svc_cat',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='services_module.services', verbose_name='دسته بندی'),
        ),
    ]
