# Generated by Django 3.2.25 on 2024-09-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0006_contactussetting_keyword_four'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactussetting',
            name='keyword_four',
            field=models.CharField(blank=True, help_text='یک کلمه کلیدی برای افزایش رتبه گوگل یا سئو ، متناسب با محتوای این صفحه بنویسید', max_length=160, null=True, verbose_name='کلمه کلیدی چهارم'),
        ),
    ]
