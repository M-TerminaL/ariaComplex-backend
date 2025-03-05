# Generated by Django 3.2.25 on 2024-08-08 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services_module', '0016_auto_20240807_0643'),
        ('order_module', '0019_alter_orderdetail_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='package',
            field=models.ForeignKey(help_text='برای اطمینان بیشتر ، از مراجعه کننده نام شخص یا شماره تلفن همراه و نام پکیج خریداری شده را سوال کنید.', on_delete=django.db.models.deletion.CASCADE, to='services_module.tablepricesrows', verbose_name='پکیج'),
        ),
    ]
