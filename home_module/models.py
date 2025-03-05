from django.db import models
from services_module.models import Services


# Create your models here.

class HomeServices(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان خدمات')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    work_time = models.CharField(max_length=200, verbose_name='ساعات کاری')
    bg_img = models.ImageField(upload_to='home-services/svc-images', verbose_name='تصویر پس زمینه')
    svc_cat = models.OneToOneField(Services, on_delete=models.CASCADE, verbose_name='دسته بندی', related_name='services')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'آیتم خدمات'
        verbose_name_plural = 'خدمات مجموعه'

    def __str__(self):
        return self.title


class Slider(models.Model):
    img_slider = models.ImageField(upload_to='home-services/svc-images', verbose_name='تصویر اسلایدر')
    slider_cat = models.ForeignKey(HomeServices, on_delete=models.CASCADE, verbose_name='دسته خدمات',
                                   related_name='sliders')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.slider_cat.title


class ItemsService(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    item_cat = models.ForeignKey(HomeServices, on_delete=models.CASCADE, verbose_name='دسته خدمات',
                                 related_name='items')

    class Meta:
        verbose_name = 'آیتم امکانات'
        verbose_name_plural = 'امکانات خدمات'

    def __str__(self):
        return self.title
