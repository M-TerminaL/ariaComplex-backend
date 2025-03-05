from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class PurchaseMethod(models.Model):
    orange_title = models.CharField(max_length=150, verbose_name='عنوان طلایی رنگ', default='منتظر حضور گرمتان هستیم')
    black_title = models.CharField(max_length=150, verbose_name='عنوان مشکی رنگ', default='باشگاه تشریفاتی آریا')
    image_one = models.ImageField(upload_to='services/building', verbose_name='تصویر اول از نمای مجموعه')
    image_two = models.ImageField(upload_to='services/building', verbose_name='تصویر دوم از نمای مجموعه')
    short_description = models.CharField(max_length=400, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    imp_description = models.CharField(max_length=400, verbose_name='توضیحات مهم')

    class Meta:
        verbose_name = 'توضیحات آموزشی'
        verbose_name_plural = 'توضیحات اموزشی خرید از سایت'

    def __str__(self):
        return f'( {self.orange_title} ), ( {self.black_title} )'


# The Model of Services Detail page
class Services(models.Model):
    title = models.CharField(max_length=40, verbose_name='عنوان', help_text='عنوان خدمات را بنویسید')
    english_name = models.CharField(max_length=300, verbose_name='عنوان خدمات به انگلیسی',
                                    default='swimming pool',
                                    help_text='برای عنوان خدمات این صفحه از ترکیب یک یا چند کلمه انگلیسی استفاده کنید مانند مثال داخل فیلد که برای عنوان خدمات استخر در نظر گرفته شده.')
    slug = models.SlugField(default='', db_index=True, max_length=200, verbose_name='عنوان در url',
                            unique=True,
                            help_text='ترجیحا در این فیلد تغییر ایجاد نکنید و این فیلد متناسب با نام انگلیسی در نظر گرفته شده در فیلد قبلی به صورت خودکار تولید می شود.')
    order = models.IntegerField(verbose_name='اولویت بر اساس عدد',
                                help_text='برای هر خدمات یک اولیت بر اساس عدد تایین کنید تا به ترتیب اولیت شما در وب سایت دیده شود')
    header_img = models.ImageField(upload_to='services/header_images', verbose_name='تصویر هدر')
    title_img_header = models.CharField(max_length=40, verbose_name='عنوان روی تصویر هدر')
    short_description_of_img_header = models.TextField(verbose_name='توضیحات کوتاه روی تصویر هدر', null=True,
                                                       blank=True)
    introduce_title = models.CharField(max_length=50, verbose_name='عنوان بخش توضیحات', default='معرفی خدمات ما')
    purchase_category = models.ForeignKey(PurchaseMethod, on_delete=models.PROTECT, verbose_name='نحوه خرید از وب سایت',
                                          related_name='purchase')
    discount_title = models.CharField(max_length=100, verbose_name='عنوان نمایشی تخفیف', null=True, blank=True)
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
    keyword_five = models.CharField(max_length=160, verbose_name='کلمه کلیدی پنجم', null=True, blank=True,
                                    help_text='یک کلمه کلیدی برای افزایش رتبه گوگل یا سئو ، متناسب با محتوای این صفحه بنویسید')
    keyword_six = models.CharField(max_length=160, verbose_name='کلمه کلیدی ششم', null=True, blank=True,
                                   help_text='یک کلمه کلیدی برای افزایش رتبه گوگل یا سئو ، متناسب با محتوای این صفحه بنویسید')
    keyword_seven = models.CharField(max_length=160, verbose_name='کلمه کلیدی هفتم', null=True, blank=True,
                                     help_text='یک کلمه کلیدی برای افزایش رتبه گوگل یا سئو ، متناسب با محتوای این صفحه بنویسید')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال', default=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'آیتم خدمات'
        verbose_name_plural = 'خدمات مجموعه'

    def __str__(self):
        return self.title


class ServicesItemsBox(models.Model):
    title = models.CharField(max_length=70, verbose_name='عنوان بخش امکانات', default='امکانات بخش استخر')
    image_icon = models.ImageField(upload_to='services/icons', verbose_name='آیکن بخش امکانات', null=True, blank=True)
    category = models.OneToOneField(Services, on_delete=models.CASCADE, verbose_name='دسته خدمات',
                                    related_name='items_box')

    class Meta:
        verbose_name = 'باکس امکانات'
        verbose_name_plural = 'باکس های امکانات'

    def __str__(self):
        return f'{self.title} - ({self.category.title})'


class ServiceItems(models.Model):
    title_item = models.CharField(max_length=30, verbose_name='عنوان')
    category = models.ForeignKey(ServicesItemsBox, on_delete=models.CASCADE, verbose_name='دسته بخش امکانات',
                                 related_name='items')

    class Meta:
        verbose_name = 'آیتم امکانات'
        verbose_name_plural = 'امکانات خدمات'

    def __str__(self):
        return self.title_item


class IntroducingTheServicesBox(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان', null=False)
    icon = models.ImageField(upload_to='services/icons', verbose_name='آیکن', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات اول')
    description_two = models.TextField(verbose_name='توضیحات دوم', null=True, blank=True, help_text='درصورت نیاز می توانید توضیحات اضافه در خط جدید برای این بخش در نظر بگیرید')
    description_three = models.TextField(verbose_name='توضیحات سوم', null=True, blank=True, help_text='درصورت نیاز می توانید توضیحات اضافه در خط جدید برای این بخش در نظر بگیرید')
    description_four = models.TextField(verbose_name='توضیحات چهارم', null=True, blank=True, help_text='درصورت نیاز می توانید توضیحات اضافه در خط جدید برای این بخش در نظر بگیرید')
    services_category = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='دسته خدمات',
                                          related_name='introduce_svc_box')

    class Meta:
        verbose_name = 'توضیحات یک آیتم خدمات'
        verbose_name_plural = 'باکس های توضیحات'

    def __str__(self):
        return self.title


class MoreDetailsIntroducing(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    introducing_services_category = models.ForeignKey(IntroducingTheServicesBox, on_delete=models.CASCADE,
                                                      verbose_name='دسته توضیحات', related_name='more_detail_introduce')

    class Meta:
        verbose_name = 'توضیحات بیشتر یک آیتم خدمات'
        verbose_name_plural = 'توضیحات بیشتر خدمات'

    def __str__(self):
        return self.title


class TablePricesBox(models.Model):
    title = models.CharField(max_length=20, verbose_name='عنوان جدول', unique=True)
    category = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='دسته خدمات',
                                 related_name='table_price_box')

    class Meta:
        verbose_name = 'عنوان جدول'
        verbose_name_plural = 'عنوان جداول'

    def __str__(self):
        return self.title

    def priority(self):
        return self.table_prices_rows.all().order_by('order')


class TablePricesRows(models.Model):
    package_name = models.CharField(max_length=300, verbose_name='نام پکیج')
    package_description = models.TextField(verbose_name='توضیحات پکیج', null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت (تومان)')
    order = models.IntegerField(verbose_name='اولویت بر اساس عدد',
                                help_text='برای هر خدمات یک اولیت بر اساس عدد تایین کنید تا به ترتیب اولیت شما در وب سایت دیده شود')
    discount_title = models.CharField(max_length=100, verbose_name='عنوان نمایشی تخفیف', null=True, blank=True)
    discount_number = models.IntegerField(verbose_name='درصد تخفیف',
                                          validators=[MinValueValidator(0), MaxValueValidator(100)], default=0,
                                          null=True, blank=True)
    discount_price = models.IntegerField(verbose_name='قیمت با تخفیف', editable=False, default=0)
    category = models.ForeignKey(TablePricesBox, on_delete=models.CASCADE, verbose_name='دسته جدول',
                                 related_name='table_prices_rows')

    class Meta:
        verbose_name = 'پکیج'
        verbose_name_plural = 'پکیج ها و قیمت ها'

    def __str__(self):
        return f'{self.package_name} - ({self.price})'


class ServicesSliderBox(models.Model):
    title = models.CharField(max_length=30, verbose_name='عنوان باکس اسلایدر', default='گالری تصاویر')
    background_img = models.ImageField(upload_to='services/slider', verbose_name='تصویر پس زمینه باکس اسلایدر')
    category_services = models.OneToOneField(Services, on_delete=models.CASCADE, verbose_name='دسته خدمات',
                                             related_name='svc_slider_box')

    class Meta:
        verbose_name = 'باکس اسلایدر'
        verbose_name_plural = 'باکس های اسلایدر'

    def __str__(self):
        return self.category_services.title


class ServicesSlider(models.Model):
    image_slider = models.ImageField(upload_to='services/slider', verbose_name='تصویر اسلایدر')
    category = models.ForeignKey(ServicesSliderBox, on_delete=models.CASCADE, verbose_name='دسته باکس اسلایدر',
                                 related_name='svc_slider')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.category.category_services.title
