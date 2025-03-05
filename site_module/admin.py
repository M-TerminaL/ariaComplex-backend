from django.contrib import admin
from .models import *
from django.utils.html import format_html


# Register your models here.


class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_main_setting']


class TitleDescriptionHomeSliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']


class HomeSliderAdmin(admin.ModelAdmin):
    def image(self, obj):
        return format_html(f'<img src="{obj.desktop_img.url}" style="width:200px; height:80px"/>')

    list_display = ['image', 'title', 'is_active']
    list_per_page = 5
    list_filter = ['is_active']
    list_editable = ['title', 'is_active']


admin.site.register(SiteSetting, SiteSettingAdmin)
admin.site.register(TitleDescriptionHomeSlider, TitleDescriptionHomeSliderAdmin)
admin.site.register(HomeSlider, HomeSliderAdmin)
