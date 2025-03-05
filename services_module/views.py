from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Services, PurchaseMethod


# Create your views here.

def services_detail(request, slug):
    try:
        service = Services.objects.prefetch_related('purchase_category',
                                                    'items_box',
                                                    'items_box__items',
                                                    'introduce_svc_box',
                                                    'introduce_svc_box__more_detail_introduce',
                                                    'table_price_box',
                                                    'table_price_box__table_prices_rows',
                                                    'svc_slider_box',
                                                    'svc_slider_box__svc_slider').get(slug=slug, is_active=True)

        context = {
            'service': service
        }
        return render(request, 'services_module/services_detail_page.html', context)
    except Services.DoesNotExist:
        raise Http404()


class PricesTableView(TemplateView):
    template_name = 'services_module/prices_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        purchase: PurchaseMethod = PurchaseMethod.objects.first()
        services: Services = Services.objects.filter(is_active=True).prefetch_related(
            'table_price_box',
            'table_price_box__table_prices_rows',
            'purchase_category',
        ).only('title', 'is_active', 'slug', 'discount_title', 'purchase_category_id').all().order_by('order')
        context['services'] = services
        context['purchase'] = purchase
        return context

