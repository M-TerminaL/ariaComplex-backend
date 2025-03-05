from django.db import models


# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='نام شما')
    email = models.EmailField(max_length=300, verbose_name='ایمیل شما')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    subject = models.CharField(max_length=300, verbose_name='موضوع')
    text = models.TextField(verbose_name='پیام شما')
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'


class ContactUsSetting(models.Model):
    header_title = models.CharField(max_length=40, verbose_name='عنوان هدر')
    header_img = models.ImageField(upload_to='services/header_images', verbose_name='تصویر هدر')
    header_phone_title = models.CharField(max_length=200, verbose_name='عنوان جدول شماره تماس ها')
    building_img_one = models.ImageField(upload_to='site-setting/home-slider', verbose_name='تصویر کوچک اول')
    building_img_two = models.ImageField(upload_to='site-setting/home-slider', verbose_name='تصویر کوچک دوم')
    title_sm_img_one = models.CharField(max_length=200, verbose_name='متن کوتاه تبلیغاتی اول')
    title_sm_img_two = models.CharField(max_length=200, verbose_name='متن کوتاه تبلیغاتی دوم')
    address = models.TextField(verbose_name='آدرس')
    addr_link = models.TextField(verbose_name='لینک آدرس گوگل مپ')
    meta_description = models.CharField(max_length=160, verbose_name='متاتگ برای سئو', null=True, blank=True,
                                        help_text='برای افزایش سئو یک متن 160 کاراکتری ، ترغیب کننده ، جذاب و مرتبط با محتوای قرار گرفته در این صفحه بنویسید.')
    keyword_one = models.CharField(max_length=160, verbose_name='کلمه کلیدی اول', null=True, blank=True,
                                   help_text='یک کلمه کلیدی برای افزایش رتبه گوگل یا سئو ، متناسب با محتوای این صفحه بنویسید')
    keyword_two = models.CharField(max_length=160, verbose_name='کلمه کلیدی دوم', null=True, blank=True,
                                   help_text='یک کلمه کلیدی برای افزایش رتبه گوگل یا سئو ، متناسب با محتوای این صفحه بنویسید')
    keyword_three = models.CharField(max_length=160, verbose_name='کلمه کلیدی سوم', null=True, blank=True,
                                     help_text='یک کلمه کلیدی برای افزایش رتبه گوگل یا سئو ، متناسب با محتوای این صفحه بنویسید')
    keyword_four = models.CharField(max_length=160, verbose_name='کلمه کلیدی چهارم', null=True, blank=True,
                                     help_text='یک کلمه کلیدی برای افزایش رتبه گوگل یا سئو ، متناسب با محتوای این صفحه بنویسید')
    is_main_setting = models.BooleanField(default=False, verbose_name='تنظیمات اصلی',
                                          help_text='فقط یک تنظیمات اصلی برای صفحه تماس با ما مجاز هستید داشته باشید')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات صفحه تماس با ما'

    def __str__(self):
        return self.header_title


class PhoneTable(models.Model):
    the_part = models.CharField(max_length=150, verbose_name='بخش')
    phone = models.CharField(max_length=100, verbose_name='شماره تماس')
    setting_category = models.ForeignKey(ContactUsSetting, on_delete=models.CASCADE, verbose_name='دسته تنظیمات',
                                         related_name='phone_table')

    class Meta:
        verbose_name = 'شماره بخش'
        verbose_name_plural = 'شماره تماس بخش های مجموعه'

    def __str__(self):
        return self.the_part
