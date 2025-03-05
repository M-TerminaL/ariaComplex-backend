from django.db import models
from django.contrib.auth.models import AbstractUser
from kavenegar import *
from aria_complex_project.settings import Kavenegar_API


def send_group_message(mobile, text):
    mobile = [mobile, ]
    # text = [text, ]
    try:
        api = KavenegarAPI(Kavenegar_API)
        params = {
            'receptor': mobile,  # multiple mobile number, split by comma
            'message': text,
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


# Create your models here.

class MyUser(AbstractUser):
    username = models.CharField(max_length=11, verbose_name='شماره موبایل', unique=True, db_index=True)
    first_name = models.CharField(max_length=25, verbose_name='نام')
    last_name = models.CharField(max_length=70, verbose_name='نام خانوادگی')
    otp = models.PositiveIntegerField(blank=True, null=True, verbose_name='رمز یک بار مصرف')
    otp_create_time = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='user-profile/images', verbose_name='تصویر آواتار', null=True, blank=True)
    is_blocked = models.BooleanField(default=False, verbose_name='مسدود شده / نشده')
    failed_login_attempts = models.IntegerField(default=0)
    last_failed_login_attempt = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.username


class UserTicket(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='کاربر')
    subject = models.CharField(max_length=300, verbose_name='موضوع')
    text = models.TextField(verbose_name='پیام شما')
    image = models.ImageField(upload_to='user-tickets', verbose_name='تصویر', null=True, blank=True)
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'لیست تیکت ها'


class Announcements(models.Model):
    text = models.TextField(verbose_name='متن اطلاعیه')
    created_date = models.DateField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'اطلاعیه'
        verbose_name_plural = 'اطلاعیه ها'


class MessageBox(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='کاربر')
    text = models.TextField(verbose_name='متن پیام')
    created_date = models.DateField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class MessageGroupKavehNegar(models.Model):
    subject = models.CharField(max_length=200, verbose_name='عنوان پیام',
                               help_text='عنوان پیام صرفا برای نمایش مشخصه ای از پیام در لیست پیام های گروهی کاربرد دارد')
    text = models.TextField(verbose_name='متن پیام')

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        my_user = MyUser.objects.filter(is_active=True)
        for user in my_user:
            send_group_message(user.username, self.text)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'لیست پیام های گروهی با پنل پیامکی'
