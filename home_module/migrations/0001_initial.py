# Generated by Django 3.2.25 on 2024-07-16 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان خدمات')),
                ('short_description', models.TextField(verbose_name='توضیحات کوتاه')),
                ('work_time', models.CharField(max_length=200, verbose_name='ساعات کاری')),
                ('bg_img', models.ImageField(upload_to='home-services/svc-images', verbose_name='تصویر پس زمینه')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'آیتم خدمات',
                'verbose_name_plural': 'خدمات مجموعه',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_slider', models.ImageField(upload_to='home-services/svc-images', verbose_name='تصویر اسلایدر')),
                ('slider_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sliders', to='home_module.homeservices', verbose_name='دسته خدمات')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
            },
        ),
        migrations.CreateModel(
            name='ItemsService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('item_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='home_module.homeservices', verbose_name='دسته خدمات')),
            ],
            options={
                'verbose_name': 'آیتم امکانات',
                'verbose_name_plural': 'امکانات خدمات',
            },
        ),
    ]
