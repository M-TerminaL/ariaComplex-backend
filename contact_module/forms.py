from django import forms
from .models import ContactUs
from django.core.exceptions import ValidationError
from django.core import validators


class ContactUsForm(forms.Form):
    full_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'exampleFormControlInput1',
        'type': 'text'
    }), validators=[validators.MaxLengthValidator(50),
                    validators.RegexValidator(regex=r'[\u0621-\u06cc\u00ab\u00bb\u060c\u061b]+',
                                              message='*نام و نام خانوادگی را به فارسی بنویسید')])
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'exampleFormControlInput2',
    }), validators=[validators.EmailValidator(), validators.MaxLengthValidator(100)])
    phone = forms.CharField(max_length=11, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'exampleFormControlInput3',
        'type': 'tel'
    }))
    subject = forms.CharField(max_length=300, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'exampleFormControlInput4',
        'type': 'text'
    }))
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'exampleFormControlTextarea1',
        'rows': 6
    }))

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise ValidationError('*فیلد شماره تماس باید عددی باشد')
        return phone
