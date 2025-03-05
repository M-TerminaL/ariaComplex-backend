from django.shortcuts import render
from django.views.generic import TemplateView
from home_module.models import HomeServices
from home_module.signals import get_site_setting, get_home_services, get_home_slider
from order_module.models import OrderDetail
from site_module.models import HomeSlider, TitleDescriptionHomeSlider
from services_module.models import Services

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # sliders = HomeSlider.objects.filter(is_active=True)
        sliders = get_home_slider()
        title_des_slider = TitleDescriptionHomeSlider.objects.filter(is_active=True).first()
        # services: HomeServices = HomeServices.objects.filter(is_active=True).prefetch_related(
        #     'sliders', 'items', 'svc_cat').only(
        #     'svc_cat__slug',
        #     'bg_img',
        #     'title',
        #     'work_time',
        #     'short_description',
        #     'is_active',
        # )
        services = get_home_services()    # get data from cache
        context['sliders'] = sliders
        context['title_des_slider'] = title_des_slider
        context['services'] = services
        return context


def site_header_component(request):
    setting = get_site_setting()  # get data from cache
    services: Services = Services.objects.filter(is_active=True).only('title', 'slug').order_by('order')
    user_basket_count = OrderDetail.objects.filter(order__user_id=request.user.id, order__is_paid=False).count()
    context = {
        'site_setting': setting,
        'services': services,
        'user_basket_count': user_basket_count
    }
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    setting = get_site_setting()    # get data from cache
    context = {
        'site_setting': setting
    }
    return render(request, 'shared/site_footer_component.html', context)
