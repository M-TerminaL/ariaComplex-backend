# Generated by Django 3.2.25 on 2024-08-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0005_alter_contactussetting_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactussetting',
            name='keyword_four',
            field=models.CharField(blank=True, help_text='یک کلمه کلیدی برای افزایش رتبه گوگل یا سئو ، متناسب با محتوای این صفحه بنویسید', max_length=160, null=True, verbose_name='کلمه کلیدی سوم'),
        ),
    ]
