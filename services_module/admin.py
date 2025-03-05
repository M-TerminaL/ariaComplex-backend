from django.contrib import admin
from . import models
from django.utils.html import format_html
from jalali_date import datetime2jalali


# Register your models here.


class ServicesAdmin(admin.ModelAdmin):
    search_fields = ['title']
    prepopulated_fields = {
        'slug': ['english_name']
    }
    list_display = ['__str__', 'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active']
    list_per_page = 15


class ServicesItemsBoxAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['__str__', 'category']
    list_editable = ['category']
    list_filter = ['category']
    list_per_page = 15


class ServiceItemsAdmin(admin.ModelAdmin):
    search_fields = ['title_item']
    list_display = ['__str__', 'category']
    list_filter = ['category']
    list_editable = ['category']
    list_per_page = 20


class ServicesSliderBoxAdmin(admin.ModelAdmin):

    def image_bg(self, obj):
        return format_html(f'<img src="{obj.background_img.url}" style="max-width:100px; max-height:100px"/>')

    list_display = ['__str__', 'image_bg', 'category_services']
    list_editable = ['category_services']
    list_filter = ['category_services']
    list_per_page = 10


class ServicesSliderAdmin(admin.ModelAdmin):

    def image(self, obj):
        return format_html(f'<img src="{obj.image_slider.url}" style="max-width:100px; max-height:100px"/>')

    search_fields = ['category']
    list_display = ['__str__', 'image', 'category']
    # readonly_fields = ['image']
    list_editable = ['category']
    list_filter = ['category']
    list_per_page = 10


class TablePricesBoxAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['__str__', 'category']
    list_filter = ['category']
    list_editable = ['category']
    list_per_page = 20


class TablePricesRowsAdmin(admin.ModelAdmin):
    search_fields = ['package_name', 'price']
    list_display = ['__str__', 'price', 'category', 'order']
    list_filter = ['category']
    list_editable = ['price', 'category', 'order']
    list_per_page = 20


class IntroducingTheServicesBoxAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['__str__', 'services_category']
    list_filter = ['services_category']
    list_editable = ['services_category']
    list_per_page = 20


class MoreDetailsIntroducingAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['__str__', 'introducing_services_category']
    list_editable = ['introducing_services_category']
    list_filter = ['introducing_services_category']
    list_per_page = 20


class PurchaseMethodAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    list_per_page = 5


admin.site.register(models.Services, ServicesAdmin)
admin.site.register(models.ServicesItemsBox, ServicesItemsBoxAdmin)
admin.site.register(models.ServiceItems, ServiceItemsAdmin)
admin.site.register(models.ServicesSliderBox, ServicesSliderBoxAdmin)
admin.site.register(models.ServicesSlider, ServicesSliderAdmin)
admin.site.register(models.TablePricesBox, TablePricesBoxAdmin)
admin.site.register(models.TablePricesRows, TablePricesRowsAdmin)
admin.site.register(models.IntroducingTheServicesBox, IntroducingTheServicesBoxAdmin)
admin.site.register(models.MoreDetailsIntroducing, MoreDetailsIntroducingAdmin)
admin.site.register(models.PurchaseMethod, PurchaseMethodAdmin)
