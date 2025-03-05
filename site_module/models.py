from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    site_logo = models.ImageField(upload_to='site-setting/logo', verbose_name='لوگوی سایت')
    slogan_one = models.CharField(max_length=200, verbose_name='شعار مشکی رنگ')
    slogan_two = models.CharField(max_length=200, verbose_name='شعار طلایی رنک')
    phone_notif = models.CharField(max_length=50, verbose_name='تلفن بدون پیش شماره')
    phone_header = models.CharField(max_length=50, verbose_name='تلفن با کد شهر')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    working_time = models.CharField(max_length=200, verbose_name='ساعات کاری')
    about_des = models.TextField(verbose_name='توضیحات کوتاه معرفی سایت')
    instagram = models.CharField(max_length=100, verbose_name='آی دی اینستاگرام')
    whatsapp = models.CharField(max_length=100, verbose_name='شماره واتس آپ')
    telegram = models.CharField(max_length=100, verbose_name='آی دی تلگرام')
    youtube_link = models.URLField(verbose_name='لینک یوتیوب')
    location_link = models.URLField(verbose_name='لینک لوکیشن')
    copy_right = models.TextField(verbose_name='متن کپی رایت')
    developer = models.CharField(max_length=200, verbose_name='متن معرفی طراح و توسعه دهنده')
    footer_img = models.ImageField(upload_to='site-setting/footer-images', verbose_name='تصویر پس زمینه فوتر')
    samandehi_img = models.ImageField(upload_to='site-setting/footer-images', verbose_name='تصویر سامان دهی', null=True, blank=True, help_text='اختیاری')
    samandehi_url = models.URLField(verbose_name='لینک ساماندهی', help_text='اختیاری', null=True, blank=True)
    enamad_img = models.ImageField(upload_to='site-setting/footer-images', verbose_name='تصویر ای نماد', null=True, blank=True, help_text='اختیاری')
    enamad_url = models.URLField(verbose_name='لینک ای نماد', help_text='اختیاری', null=True, blank=True)
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی', help_text='فقط مجاز هستید یک تنظیمات اصلی داشته باشید.')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'


class TitleDescriptionHomeSlider(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان', help_text='عنوان روی اسلایدر اصلی در صفحه اصلی')
    description = models.TextField(verbose_name='توضیحات کوتاه', help_text='توضیحات کوتاه روی اسلایدر اصلی در صفحه اصلی')
    meta_description = models.CharField(max_length=160, verbose_name='متاتگ برای سئو', null=True, blank=True,
                                        help_text='برای افزایش سئو یک متن 160 کاراکتری ، ترغیب کننده ، جذاب و مرتبط با محتوای قرار گرفته در صفحه اصلی سایت بنویسید.')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال', help_text='فقط یک عنوان و توضیحات روی اسلایدر صفحه اصلی سایت مجاز می باشد.')

    class Meta:
        verbose_name = 'عنوان و توضیحات اسلایدر'
        verbose_name_plural = 'عنوان و توضیحات اسلایدر'

    def __str__(self):
        return self.title


class HomeSlider(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    # mobile_img = models.ImageField(upload_to='site-setting/home-slider', verbose_name='تصویر اسلایدر در ابعاد موبایل')
    desktop_img = models.ImageField(upload_to='site-setting/home-slider', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر های اصلی'

    def __str__(self):
        return self.title
