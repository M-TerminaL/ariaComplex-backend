# Generated by Django 3.2.25 on 2024-08-08 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0011_auto_20240808_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(help_text='در این فیلد با فشردن روی آیکن مداد زرد رنگ وارد سبد خرید کاربر شوید و فیلد نهایی شده / نشده را بررسی کنید', on_delete=django.db.models.deletion.CASCADE, to='order_module.order', verbose_name='سبد خرید'),
        ),
    ]
