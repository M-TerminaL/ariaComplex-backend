import datetime
from kavenegar import *
from aria_complex_project.settings import Kavenegar_API
from random import randint
from account_module.models import MyUser
from django.utils import timezone
from background_task import background



# @background(schedule=1)
def send_otp(mobile, otp):
    mobile = [mobile, ]
    try:
        api = KavenegarAPI(Kavenegar_API)
        params = {
            'sender': '2000500666',  # optional
            'template': 'verify',
            'token': str(otp),
            'receptor': mobile,  # multiple mobile number, split by comma
            'type': 'sms'
        }
        response = api.verify_lookup(params)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)



def get_random_otp():
    return randint(10000, 99999)


def check_otp_expiration(mobile):
    try:
        user = MyUser.objects.get(username=mobile)
        now = timezone.now()
        otp_time = user.otp_create_time
        diff_time = now - otp_time
        expiration_time = datetime.timedelta(seconds=120)

        if diff_time > expiration_time:
            return False  # رمز منقضی شده است
        return True
    except MyUser.DoesNotExist:
        return False

# def check_otp_time(mobile):
#     try:
#         user = MyUser.objects.get(username=mobile)
#         now = timezone.now()
#         otp_time = user.otp_create_time
#         diff_time = now - otp_time
#         expiration_time = datetime.timedelta(seconds=120)
#
#         if diff_time


def send_welcome_msg(mobile, name):
    mobile = [mobile, ]
    try:
        api = KavenegarAPI(Kavenegar_API)
        params = {
            'receptor': mobile,  # multiple mobile number, split by comma
            'message': f'{name} عزیز ، ثبت نام شما با موفقیت انجام شد \n به وب اپلیکیشن مجموعه فرهنگی ورزشی آریا خوش آمدید.',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
