# Generated by Django 3.2.25 on 2024-09-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_module', '0022_tablepricesrows_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='introducingtheservicesbox',
            name='description_four',
            field=models.TextField(blank=True, help_text='درصورت نیاز می توانید توضیحات اضافه در خط جدید برای این بخش در نظر بگیرید', null=True, verbose_name='توضیحات چهارم'),
        ),
        migrations.AddField(
            model_name='introducingtheservicesbox',
            name='description_three',
            field=models.TextField(blank=True, help_text='درصورت نیاز می توانید توضیحات اضافه در خط جدید برای این بخش در نظر بگیرید', null=True, verbose_name='توضیحات سوم'),
        ),
        migrations.AddField(
            model_name='introducingtheservicesbox',
            name='description_two',
            field=models.TextField(blank=True, help_text='درصورت نیاز می توانید توضیحات اضافه در خط جدید برای این بخش در نظر بگیرید', null=True, verbose_name='توضیحات دوم'),
        ),
        migrations.AlterField(
            model_name='introducingtheservicesbox',
            name='description',
            field=models.TextField(verbose_name='توضیحات اول'),
        ),
    ]
