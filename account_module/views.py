import time
from datetime import datetime, timedelta
from django.utils import timezone
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import login, logout
from account_module.forms import RegisterForm, ActiveForm, LoginForm, LoginPassVerifyForm
from account_module.models import MyUser
from .helper import send_otp, get_random_otp, check_otp_expiration, send_welcome_msg


# Create your views here.


class RegisterView(View):
    def get(self, request: HttpRequest):
        if not request.user.is_authenticated:
            register_form = RegisterForm()
            context = {
                'register_form': register_form
            }
            return render(request, 'account_module/register.html', context)
        else:
            return redirect(reverse('user_panel_dashboard_page'))

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            mobile = register_form.cleaned_data.get('mobile')
            first_name = register_form.cleaned_data.get('first_name')
            last_name = register_form.cleaned_data.get('last_name')
            otp = get_random_otp()
            user = MyUser.objects.filter(username__iexact=mobile).exists()

            if user:
                main_user = MyUser.objects.filter(username__iexact=mobile).first()
                if main_user.is_active:
                    register_form.add_error('mobile', '*شماره موبایل وارد شده تکراری می باشد')
                else:
                    main_user.delete()
                    register_form.add_error('mobile', '*شماره موبایل وارد شده غیرفعال است دوباره ثبت نام کنید')

            else:
                new_user = MyUser(
                    username=mobile,
                    first_name=first_name,
                    last_name=last_name,
                    is_active=False,
                    otp=otp
                )
                new_user.set_password('AriaComplex')
                new_user.save()
                send_otp(mobile, otp)
                request.session['user_mobile'] = mobile
                return redirect(reverse('activate_account_page'))

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)


class ActivateAccountView(View):
    def get(self, request: HttpRequest):
        if not request.user.is_authenticated:
            activate_form = ActiveForm()
            is_timer_active = True
            context = {
                'activate_form': activate_form,
                'is_timer_active': is_timer_active
            }
            return render(request, 'account_module/activate_account.html', context)
        else:
            return redirect(reverse('user_panel_dashboard_page'))

    def post(self, request: HttpRequest):
        activate_form = ActiveForm(request.POST)
        if activate_form.is_valid():
            otp_1 = activate_form.cleaned_data.get('one')
            otp_2 = activate_form.cleaned_data.get('two')
            otp_3 = activate_form.cleaned_data.get('three')
            otp_4 = activate_form.cleaned_data.get('four')
            otp_5 = activate_form.cleaned_data.get('five')
            concat_otp = otp_1 + otp_2 + otp_3 + otp_4 + otp_5
            mobile = request.session.get('user_mobile')

            if mobile is not None:
                user = MyUser.objects.filter(username=mobile).first()
                if user is not None:
                    if user.is_active:
                        return redirect(reverse('login_page'))
                    else:
                        if not check_otp_expiration(mobile):
                            user.delete()
                            del request.session['user_mobile']
                            is_timer_active = False
                            return render(request, 'account_module/activate_account.html',
                                          {'err1': 'رمز عبور یک بار مصرف منقضی شده است',
                                           'activate_form': activate_form,
                                           'is_timer_active': is_timer_active})
                        elif user.otp != int(concat_otp):
                            is_timer_active = False
                            return render(request, 'account_module/activate_account.html',
                                          {'err': 'کد وارد شده نا معتبر می باشد', 'activate_form': activate_form,
                                           'is_timer_active': is_timer_active})
                        else:
                            user.is_active = True
                            user.otp = None
                            user.save()
                            login(request, user)
                            # send_welcome_msg(mobile, user.first_name)
                            del request.session['user_mobile']
                            return redirect(reverse('user_panel_dashboard_page'))
                else:
                    return redirect(reverse('register_page'))
            else:
                return redirect(reverse('register_page'))

        context = {
            'activate_form': activate_form
        }
        return render(request, 'account_module/activate_account.html', context)


class LoginView(View):
    def get(self, request: HttpRequest):
        if not request.user.is_authenticated:
            login_form = LoginForm()
            context = {
                'login_form': login_form
            }
            return render(request, 'account_module/login.html', context)
        else:
            return redirect(reverse('user_panel_dashboard_page'))

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            mobile = login_form.cleaned_data.get('mobile')
            user = MyUser.objects.filter(username=mobile).first()
            if user is not None:
                if user.is_active:
                    if user.is_blocked:
                        if user.last_failed_login_attempt:
                            if timezone.now() - user.last_failed_login_attempt > timedelta(minutes=60):
                                user.is_blocked = False
                                user.failed_login_attempts = 0
                                user.last_failed_login_attempt = None
                                user.save()
                            else:
                                return render(request, 'account_module/login.html',
                                              {'login_form': login_form,
                                               'err2': 'حساب شما به دلیل تلاش‌ های ناموفق متعدد مسدود شده است.'})
                        else:
                            user.last_failed_login_attempt = datetime.now()

                    elif check_otp_expiration(user.username):
                        return render(request, 'account_module/login.html',
                                      {
                                          'login_form': login_form,
                                          'err5': 'شما نمی توانید قبل از منقضی شدن رمز یک بار مصرف قبلی درخواست ارسال مجدد نمایید.'
                                      })

                    otp = user.otp = get_random_otp()
                    user.save()
                    send_otp(mobile, otp)
                    request.session['user_mobile_user'] = mobile
                    return redirect(reverse('login_sms_pass_page'))
                else:
                    user.delete()
                    return render(request, 'account_module/login.html',
                                  context={'err': 'حساب شما غیرفعال است، مراحل ثبت نام را دوباره انجام دهید',
                                           'login_form': login_form})
            else:
                return render(request, 'account_module/login.html',
                              context={'err1': 'شما در سایت ثبت نام انجام ندادید', 'login_form': login_form})

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)


class LoginSmsPassView(View):
    def get(self, request: HttpRequest):
        if not request.user.is_authenticated:
            login_sms_pass_form = LoginPassVerifyForm()
            is_timer_active = True
            context = {
                'login_sms_pass_form': login_sms_pass_form,

                'is_timer_active': is_timer_active
            }
            return render(request, 'account_module/login_sms_pass.html', context)
        else:
            return redirect(reverse('user_panel_dashboard_page'))

    def post(self, request: HttpRequest):
        login_sms_pass_form = LoginPassVerifyForm(request.POST)

        if login_sms_pass_form.is_valid():
            otp_1 = login_sms_pass_form.cleaned_data.get('one')
            otp_2 = login_sms_pass_form.cleaned_data.get('two')
            otp_3 = login_sms_pass_form.cleaned_data.get('three')
            otp_4 = login_sms_pass_form.cleaned_data.get('four')
            otp_5 = login_sms_pass_form.cleaned_data.get('five')
            concat_otp = otp_1 + otp_2 + otp_3 + otp_4 + otp_5
            mobile = request.session.get('user_mobile_user')

            if mobile is not None:
                user = MyUser.objects.filter(username=mobile).first()
                if user is not None:
                    if not user.is_active:
                        del request.session['user_mobile_user']
                        return redirect(reverse('login_page'))
                    else:
                        if not check_otp_expiration(mobile):
                            del request.session['user_mobile_user']
                            user.otp = None
                            user.save()

                            is_timer_active = False

                            return render(request, 'account_module/login_sms_pass.html',
                                          {'errr': 'رمز عبور یک بار مصرف منقضی شده است',
                                           'login_sms_pass_form': login_sms_pass_form,
                                           'is_timer_active': is_timer_active})

                        elif user.otp != int(concat_otp):
                            user.failed_login_attempts += 1
                            if not user.last_failed_login_attempt:
                                user.last_failed_login_attempt = datetime.now()
                            user.save()

                            if user.failed_login_attempts >= 3:
                                del request.session['user_mobile_user']
                                user.is_blocked = True
                                user.otp = None
                                user.save()
                                is_timer_active = False
                                return render(request, 'account_module/login_sms_pass.html',
                                              {'login_sms_pass_form': login_sms_pass_form,
                                               'err3': 'رمز وارد شده صحیح نیست. حساب شما به مدت یک ساعت مسدود شده است.',
                                               'is_timer_active': is_timer_active})
                            is_timer_active = False
                            return render(request, 'account_module/login_sms_pass.html',
                                          {'err1': 'کد وارد شده نا معتبر می باشد',
                                           'login_sms_pass_form': login_sms_pass_form,
                                           'is_timer_active': is_timer_active})
                        else:
                            user.otp = None
                            user.failed_login_attempts = 0
                            user.last_failed_login_attempt = None
                            user.save()
                            login(request, user)
                            del request.session['user_mobile_user']
                            return redirect(reverse('user_panel_dashboard_page'))
                else:
                    return redirect(reverse('register_page'))
            else:
                return redirect(reverse('login_page'))

        context = {
            'login_sms_pass_form': login_sms_pass_form
        }
        return render(request, 'account_module/login_sms_pass.html', context)


class LogoutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect(reverse('home_page'))
