# Generated by Django 3.2.25 on 2024-08-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0015_alter_orderdetail_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(help_text='حتی اگر کد رهگیری کاربر با مطالعات شما مطابقت داشت ولی سبد خرید ایشان نهایی نشده بود، فرد را از ادامه ی فرایند ثبت نام منع کنید. این رویداد هرگز رخ نخواهد داد مگر اینکه شخص مراجعه کننده، برنامه نویس ویا هکر بوده و قصد سو استفاده داشته باشد.', verbose_name='نهایی شده / نشده'),
        ),
    ]
