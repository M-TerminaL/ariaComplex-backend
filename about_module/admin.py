from django.contrib import admin
from .models import *
from django.utils.html import format_html


# Register your models here.


class AboutUsAdmin(admin.ModelAdmin):
    list_filter = ['is_main_setting']
    list_display = ['__str__', 'is_main_setting']


class ManagersAdmin(admin.ModelAdmin):
    def image(self, obj):
        return format_html(f'<img src="{obj.profile_img.url}" width="100" height="100" />')

    list_display = ['image', 'full_name', 'position', 'about_page_category']
    list_filter = ['about_page_category']
    search_fields = ['full_name']


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Managers, ManagersAdmin)
