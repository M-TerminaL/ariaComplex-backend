# Generated by Django 3.2.25 on 2024-08-05 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0013_userticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='متن اطلاعیه')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'اطلاعیه',
                'verbose_name_plural': 'اطلاعیه ها',
            },
        ),
    ]
