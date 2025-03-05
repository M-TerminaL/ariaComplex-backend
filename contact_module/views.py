from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from contact_module.forms import ContactUsForm
from contact_module.models import ContactUs, ContactUsSetting


# Create your views here.

class ContactUsView(View):
    def get(self, request):
        contact_us = ContactUsForm()
        contact_us_setting = ContactUsSetting.objects.filter(is_main_setting=True).prefetch_related('phone_table').first()
        context = {
            'contact_us': contact_us,
            'contact_us_setting': contact_us_setting
        }
        return render(request, 'contact_module/contact_us_page.html', context)

    def post(self, request):
        contact_us = ContactUsForm(request.POST)
        contact_us_setting = ContactUsSetting.objects.filter(is_main_setting=True).prefetch_related('phone_table').first()
        if contact_us.is_valid():
            contact = ContactUs(
                full_name=contact_us.cleaned_data.get('full_name'),
                email=contact_us.cleaned_data.get('email'),
                phone=contact_us.cleaned_data.get('phone'),
                subject=contact_us.cleaned_data.get('subject'),
                text=contact_us.cleaned_data.get('text')
            )
            contact.save()
            return render(request, 'contact_module/contact_us_page.html', context={
                'contact_us': contact_us,
                'contact_us_setting': contact_us_setting,
                'success': 'پیام شما با موفقیت ارسال گردید.'
            })

        context = {
            'contact_us': contact_us,
            'contact_us_setting': contact_us_setting
        }
        return render(request, 'contact_module/contact_us_page.html', context)
