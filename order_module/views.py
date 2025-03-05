# Create your views here.
import time
import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import reverse
from django.utils.crypto import get_random_string

from account_module.models import MyUser
from services_module.models import TablePricesRows
from .models import Order, OrderDetail, DiscountCode

from django.conf import settings
from django.shortcuts import redirect, render
import requests
import json


def add_package_to_order(request: HttpRequest):
    package_id = int(request.GET.get('package_id'))
    count = request.GET.get('count')

    if str(count) == '' or int(count) < 1:
        return JsonResponse({
            'status': 'invalid_count',
            'text': 'مقدار وارد شده معتبر نمی باشد',
            'confirm_button_text': 'مرسی از شما',
            'icon': 'warning'
        })

    if request.user.is_authenticated:
        package: TablePricesRows = TablePricesRows.objects.filter(id=package_id).first()
        if package is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(package_id=package_id).first()
            if current_order_detail is not None:
                current_order_detail.count += int(count)
                current_order_detail.tracking_code = get_random_string(8)
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, package_id=package_id, count=count, tracking_code=get_random_string(8))
                new_detail.save()

            return JsonResponse({
                'status': 'success',
                'text': 'پکیج مورد نظر با موفقیت به سبد خرید شما اضافه شد',
                'confirm_button_text': 'باشه ممنونم',
                'icon': 'success'
            })
        else:
            return JsonResponse({
                'status': 'Not_Found',
                'text': 'پکیج مورد نشر یافت نشد',
                'confirm_button_text': 'مرسی',
                'icon': 'error'
            })

    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای افزودن پکیج به سبد خرید ابتدا می بایست وارد سایت شوید',
            'confirm_button_text': 'باشه ممنونم',
            'icon': 'error'
        })


# ? sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

# Important: need to edit for real server.
CallbackURL = 'http://127.0.0.1:8008/order/verify-payment/'


@login_required
def request_payment(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)

    current_discount_codes = DiscountCode.objects.filter(is_active=True, user=request.user.id)
    phone: MyUser = MyUser.objects.filter(id=request.user.id, is_active=True).first()
    discount_code = request.session.get('discount_code')
    total_amount = 0
    order_details = ''

    for order_detail in current_order.orderdetail_set.all():
        if order_detail.package.discount_number and order_detail.package.discount_title:
            discount_public_amount = order_detail.package.price - (
                    order_detail.package.price * order_detail.package.discount_number / 100)
            package_instance: TablePricesRows = TablePricesRows.objects.filter(id=order_detail.package_id).first()
            package_instance.discount_price = int(discount_public_amount)
            package_instance.save()
            total_amount += int(discount_public_amount) * order_detail.count
        else:
            total_amount += order_detail.package.price * order_detail.count

    if discount_code is not None and current_discount_codes is not None:
        for code_value in current_discount_codes:
            if code_value.code == discount_code:
                print(total_amount)
                total_amount = int(total_amount - (total_amount * code_value.amount / 100))
                print(total_amount)
                break
    if total_amount == 0:
        return redirect(reverse('user_basket_page'))

    for detail in current_order.orderdetail_set.all():
        order_details += detail.package.package_name + ','

    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": total_amount,
        "Description": order_details,
        "Phone": phone.username,
        "CallbackURL": CallbackURL,
    }

    data = json.dumps(data)
    # set content length by data
    headers = {'accept': 'application/json', 'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

        if response.status_code == 200:
            response_json = response.json()
            authority = response_json['Authority']
            if response_json['Status'] == 100:
                return redirect(ZP_API_STARTPAY + authority)
            else:
                return HttpResponse('Error')
        return HttpResponse('response failed')
    except requests.exceptions.Timeout:
        return HttpResponse('Timeout Error')
    except requests.exceptions.ConnectionError:
        return HttpResponse('Connection Error')


@login_required
def verify_payment(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False, user_id=request.user.id)
    current_discount_codes = DiscountCode.objects.filter(is_active=True, user=request.user.id)
    discount_code = request.session.get('discount_code')
    total_amount = 0

    for order_detail in current_order.orderdetail_set.all():
        if order_detail.package.discount_number and order_detail.package.discount_title:
            discount_public_amount = order_detail.package.price - (
                    order_detail.package.price * order_detail.package.discount_number / 100)
            package_instance: TablePricesRows = TablePricesRows.objects.filter(id=order_detail.package_id).first()
            package_instance.discount_price = int(discount_public_amount)
            package_instance.save()
            total_amount += int(discount_public_amount) * order_detail.count
        else:
            total_amount += order_detail.package.price * order_detail.count

    if discount_code is not None and current_discount_codes is not None:
        for code_value in current_discount_codes:
            if code_value.code == discount_code:
                total_amount = int(total_amount - (total_amount * (code_value.amount / 100)))
                break
    if total_amount == 0:
        return redirect(reverse('user_basket_page'))


    authority = request.GET.get('Authority')
    status = request.GET.get('Status')
    if status == 'OK' and authority:
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": total_amount,
            "Authority": authority,
        }
        data = json.dumps(data)
        headers = {'accept': 'application/json', 'content-type': 'application/json', 'content-length': str(len(data))}
        try:
            response = requests.post(ZP_API_VERIFY, data=data, headers=headers)
            if response.status_code == 200:
                response_json = response.json()
                reference_id = response_json['RefID']
                if response_json['Status'] == 100:

                    for order_detail in current_order.orderdetail_set.all():
                        if order_detail.package.discount_number and order_detail.package.discount_title:
                            discount_public_amount = order_detail.package.price - (
                                    order_detail.package.price * order_detail.package.discount_number / 100)
                            order_detail.final_price = int(discount_public_amount)
                            order_detail.save()
                        else:
                            order_detail.final_price = order_detail.package.price
                            order_detail.save()

                    if discount_code is not None and current_discount_codes is not None:
                        for code_value in current_discount_codes:
                            if code_value.code == discount_code:
                                del request.session['discount_code']
                                code_value.delete()
                                break
                    current_order.final_order_price = total_amount
                    current_order.is_paid = True
                    current_order.payment_date = datetime.date.today()
                    current_order.save()
                    return render(request, 'order_module/payment_result.html', {
                        'success': f'تراکنش شما با کد پیگیری {reference_id} با موفقیت انجام شد'
                    })

                else:
                    return render(request, 'order_module/payment_result.html', {
                        'error1': 'تراکنش با خطا مواجه شد'
                    })

            return render(request, 'order_module/payment_result.html', {
                'error2': 'تراکنش با خطا مواجه شد'
            })
        except requests.exceptions.Timeout:
            return render(request, 'order_module/payment_result.html', {
                'error3': 'تراکنش با خطا مواجه شد. خطا در مدت زمان پرداخت'
            })
        except requests.exceptions.ConnectionError:
            return render(request, 'order_module/payment_result.html', {
                'error4': 'تراکنش با خطا مواجه شد . خطا در برقراری ارتباط . لطفا دسترسی سیستم به اینترنت را بررسی نمایید'
            })
    else:
        return render(request, 'order_module/payment_result.html', {
            'error5': 'تراکنش با خطا مواجه شد'
        })
