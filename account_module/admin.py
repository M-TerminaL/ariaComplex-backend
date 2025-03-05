from django.contrib import admin
from .models import *
from jalali_date import datetime2jalali


# Register your models here.


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'get_created_jalali', 'is_active', 'is_superuser',
                    'is_staff', 'is_blocked']
    search_fields = ['username', 'first_name', 'last_name']
    list_filter = ['is_superuser', 'is_staff', 'is_active']

    @admin.display(description='تاریخ ثبت نام', ordering='date_joined')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.date_joined).strftime('%a, %d %b %Y -|- %H:%M:%S')


class UserTicketAdmin(admin.ModelAdmin):
    list_display = ['subject', 'user', 'get_created_jalali', 'is_read_by_admin']
    list_filter = ['user', 'created_date', 'is_read_by_admin']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    list_per_page = 10

    @admin.display(description='تاریخ ایجاد', ordering='created_date')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_date).strftime('%a, %d %b %Y -|- %H:%M:%S')


class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'get_created_jalali', 'is_active']
    list_filter = ['is_active', 'created_date']
    list_per_page = 10

    @admin.display(description='تاریخ ایجاد', ordering='created_date')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_date).strftime('%a, %d %b %Y')


class MessageBoxAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'get_created_jalali', 'is_active']
    list_filter = ['is_active', 'created_date']
    list_per_page = 10

    @admin.display(description='تاریخ ایجاد', ordering='created_date')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_date).strftime('%a, %d %b %Y')

class MessageGroupKavehNegarAdmin(admin.ModelAdmin):
    list_display = ['subject']
    list_per_page = 10


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(UserTicket, UserTicketAdmin)
admin.site.register(Announcements, AnnouncementsAdmin)
admin.site.register(MessageBox, MessageBoxAdmin)
admin.site.register(MessageGroupKavehNegar, MessageGroupKavehNegarAdmin)
