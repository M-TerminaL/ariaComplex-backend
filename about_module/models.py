from django.db import models


# Create your models here.


class AboutUs(models.Model):
    header_title = models.CharField(max_length=20, verbose_name='عنوان هدر')
    header_short_description = models.TextField(verbose_name='توضیحات کوتاه هدر')
    header_img = models.ImageField(upload_to='about-us/images', verbose_name='تصویر هدر')
    video_title = models.CharField(max_length=200, verbose_name='عنوان ویدیو معرفی')
    video_link = models.URLField(verbose_name='لینک ویدیو')
    title_managers_records = models.CharField(max_length=200, verbose_name='عنوان باکس سوابق مدیران', null=True, blank=True)
    logo = models.ImageField(upload_to='about-us/images', verbose_name='تصویر لوگو')
    description_one = models.TextField(verbose_name='توضیحات اول')
    description_two = models.TextField(verbose_name='توضیحات دوم')
    meta_description = models.CharField(max_length=160, verbose_name='متاتگ برای سئو', null=True, blank=True,
                                        help_text='برای افزایش سئو یک متن 160 کاراکتری ، ترغیب کننده ، جذاب و مرتبط با محتوای قرار گرفته در این صفحه بنویسید.')
    keyword_one = models.CharField(max_length=160, verbose_name='کلمه کلیدی اول', null=True, blank=True,
                                   help_text='یک کلمه کلیدی برای افزایش رتبه گوگل یا سئو ، متناسب با محتوای این صفحه بنویسید')
    keyword_two = models.CharField(max_length=160, verbose_name='کلمه کلیدی دوم', null=True, blank=True,
                                   help_text='یک کلمه کلیدی برای افزایش رتبه گوگل یا سئو ، متناسب با محتوای این صفحه بنویسید')
    keyword_three = models.CharField(max_length=160, verbose_name='کلمه کلیدی سوم', null=True, blank=True,
                                     help_text='یک کلمه کلیدی برای افزایش رتبه گوگل یا سئو ، متناسب با محتوای این صفحه بنویسید')
    is_main_setting = models.BooleanField(default=False, verbose_name='تنظیمات اصلی',
                                          help_text='توجه: فقط یک تنظیات اصلی مجاز است')

    class Meta:
        verbose_name = 'تنظیمات صفحه درباره ما'
        verbose_name_plural = 'تنظیمات درباره ما'

    def __str__(self):
        return self.header_title


class Managers(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    position = models.CharField(max_length=30, verbose_name='سمت')
    profile_img = models.ImageField(upload_to='about-us/images', verbose_name='عکس پروفایل')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True, help_text='اختیاری')
    about_page_category = models.ForeignKey(AboutUs, on_delete=models.CASCADE,
                                            verbose_name='دسته بندی', related_name='managers')

    class Meta:
        verbose_name = 'مدیر'
        verbose_name_plural = 'مدیران'

    def __str__(self):
        return self.full_name
