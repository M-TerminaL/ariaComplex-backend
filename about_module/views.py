from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Managers, AboutUs

# Create your views here.

class AboutUsView(TemplateView):
    template_name = 'about_module/about_us_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about_us: AboutUs = AboutUs.objects.filter(is_main_setting=True).prefetch_related('managers').first()
        context['about_us'] = about_us
        return context
