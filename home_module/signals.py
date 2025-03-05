from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from home_module.models import HomeServices, Slider, ItemsService
from services_module.models import Services
from site_module.models import SiteSetting, HomeSlider


@receiver(post_delete, sender=ItemsService)
@receiver(post_delete, sender=Slider)
@receiver(post_delete, sender=HomeSlider)
@receiver(post_delete, sender=HomeServices)
@receiver(post_delete, sender=SiteSetting)
@receiver(post_save, sender=ItemsService)
@receiver(post_save, sender=Slider)
@receiver(post_save, sender=HomeSlider)
@receiver(post_save, sender=HomeServices)
@receiver(post_save, sender=SiteSetting)
def clear_cache(sender, instance, **kwargs):
    cache.clear()


def get_site_setting():
    cache_key = 'site_setting'
    setting = cache.get(cache_key)
    if not setting:
        setting = SiteSetting.objects.filter(is_main_setting=True).first()
        cache.set(cache_key, setting, 604800)  # ذخیره برای یک هفته
    return setting


def get_home_services():
    cache_key = 'home_services'
    home_svc = cache.get(cache_key)
    if not home_svc:
        home_svc: HomeServices = HomeServices.objects.filter(is_active=True).prefetch_related(
            'sliders', 'items', 'svc_cat').only(
            'svc_cat__slug',
            'bg_img',
            'title',
            'work_time',
            'short_description',
            'is_active',
        ).order_by('svc_cat__order')
        cache.set(cache_key, home_svc, 604800)  # ذخیره برای یک هقته
    return home_svc


def get_home_slider():
    cache_key = 'home_slider'
    home_slider = cache.get(cache_key)
    if not home_slider:
        home_slider: HomeSlider = HomeSlider.objects.filter(is_active=True)
        cache.set(cache_key, home_slider, 604800)  # ذخیره برای یک هفته
    return home_slider


