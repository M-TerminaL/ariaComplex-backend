from django.contrib import admin
from .models import *
from jalali_date import datetime2jalali


# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
    list_filter = ['is_read_by_admin', 'full_name', 'created_date']
    search_fields = ['phone', 'email', 'full_name']
    list_display = ['subject', 'full_name', 'get_created_jalali', 'phone', 'email', 'is_read_by_admin']
    list_per_page = 10

    @admin.display(description='تاریخ ایجاد', ordering='created_date')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_date).strftime('%a, %d %b %Y -|- %H:%M:%S')


class ContactUsSettingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_main_setting']
    list_filter = ['is_main_setting']


class PhoneTableAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'setting_category']
    search_fields = ['phone']


admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(ContactUsSetting, ContactUsSettingAdmin)
admin.site.register(PhoneTable, PhoneTableAdmin)
