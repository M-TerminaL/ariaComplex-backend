from django.contrib import admin
from home_module.models import *
from django.utils.html import format_html


# Register your models here.

class HomeServicesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active']
    list_per_page = 10


class SliderAdmin(admin.ModelAdmin):
    def image(self, obj):
        return format_html(f'<img src="{obj.img_slider.url}" width="100" height="100" />)')

    list_display = ['__str__', 'image', 'slider_cat']
    list_editable = ['slider_cat']
    list_per_page = 5
    list_filter = ['slider_cat']


class ItemsServiceAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'item_cat']
    list_filter = ['item_cat']
    list_per_page = 10


admin.site.register(HomeServices, HomeServicesAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(ItemsService, ItemsServiceAdmin)
