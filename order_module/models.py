from django.db import models
from account_module.models import MyUser
from services_module.models import TablePricesRows


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='نهایی شده / نشده',
                                  help_text='حتی اگر کد رهگیری کاربر با مطالعات شما مطابقت داشت ولی سبد خرید ایشان نهایی نشده بود، فرد را از ادامه ی فرایند ثبت نام منع کنید. این رویداد هرگز رخ نخواهد داد مگر اینکه شخص مراجعه کننده، برنامه نویس ویا هکر بوده و قصد سو استفاده داشته باشد.')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')
    final_order_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی محصولات داخل سبد خرید')

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید',
                              help_text='در این فیلد با فشردن روی آیکن مداد زرد رنگ وارد سبد خرید کاربر شوید و فیلد نهایی شده / نشده را بررسی نمایید')
    package = models.ForeignKey(TablePricesRows, on_delete=models.CASCADE, verbose_name='پکیج', help_text='برای اطمینان بیشتر ، از مراجعه کننده نام شخص یا شماره تلفن همراه و نام پکیج خریداری شده را سوال کنید.')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی پکیج')
    tracking_code = models.CharField(max_length=8, verbose_name='کد رهگیری', null=True, blank=True,
                                     help_text='در بررسی کد رهگیری کاربر دقت به عمل آورید.')
    count = models.IntegerField(verbose_name='تعداد')
    is_used = models.BooleanField(default=False, verbose_name='استفاده شده / نشده',
                                  help_text='بعد از مراجعه کاربر به پذیرش و تایید کد رهگیری ایشان ، این فیلد باید تیک خورده تا از استفاده مجدد این پکیج منع گردد.')

    def __str__(self):
        return self.package.package_name

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبدهای خرید'


class DiscountCode(models.Model):
    code = models.CharField(max_length=20, verbose_name='کد تخفیف')
    amount = models.IntegerField(verbose_name='درصد تخفیف')
    expire_date = models.CharField(max_length=200, verbose_name='تاریخ انقضا',
                                   help_text='توجه: موعد انقضای کد تخفیف فیلد مربوطه توسط ادمین حذف شود')
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT, verbose_name='کاربر')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کدهای تخفیف'

    def __str__(self):
        return self.code
