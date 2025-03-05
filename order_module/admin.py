from django.contrib import admin
from .models import *
from jalali_date import datetime2jalali


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'is_paid', 'payment_date']
    list_filter = ['is_paid', 'user', 'payment_date']
    list_per_page = 10
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    ordering = ['payment_date']

    # @admin.display(description='تاریخ پرداخت', ordering='payment_date')
    # def get_created_jalali(self, obj):
    #     return datetime2jalali(obj.payment_date).strftime('%d %b %Y')


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order', 'package', 'count', 'final_price', 'tracking_code', 'is_used']
    search_fields = ['tracking_code', 'order__user__username', 'order__user__first_name', 'order__user__last_name']
    list_filter = ['order__user__username', 'order__payment_date']
    list_per_page = 10


class DiscountCodeAdmin(admin.ModelAdmin):
    search_fields = ['expire_date', 'user__username', 'user__first_name', 'user__last_name']
    list_display = ['__str__', 'amount', 'expire_date', 'is_active', 'user']
    list_filter = ['is_active', 'user']
    list_per_page = 10


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(DiscountCode, DiscountCodeAdmin)
