from django import forms
from django.core import validators
from django.core.validators import RegexValidator

from account_module.models import MyUser


class EditProfileModelForm(forms.ModelForm):
    first_name = forms.CharField(max_length=25, required=True,
                                 validators=[RegexValidator(regex=r'[\u0621-\u06cc\u00ab\u00bb\u060c\u061b]+',
                                                            message='*نام خود را به فارسی وارد نمایید')],
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'id': 'exampleFormControlInput1'
                                 }))
    last_name = forms.CharField(max_length=70, required=True,
                                validators=[RegexValidator(regex=r'[\u0621-\u06cc\u00ab\u00bb\u060c\u061b]+',
                                                           message='*نام خانوادگی خود را به فارسی وارد نمایید')],
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'exampleFormControlInput2'
                                }))

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'avatar']
        widgets = {
            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'exampleFormControlInput3',
            })
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'avatar': ''
        }
        error_messages = {
            'first_name': {
                'required': 'وارد کردن نام اجباری می باشد ، لطفا وارد کنید'
            },
            'last_name': {
                'required': 'وارد کردن نام خانوادگی اجباری می باشد ، لطفا وارد کنید'
            }
        }


class UserTicketForm(forms.Form):
    subject = forms.CharField(max_length=300, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'exampleFormControlInput1',
        'type': 'text'
    }), validators=[validators.MaxLengthValidator(300),
                    validators.RegexValidator(regex=r'[\u0621-\u06cc\u00ab\u00bb\u060c\u061b]+',
                                              message='*موضوغ به فارسی وارد شود')])

    text = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'exampleFormControlTextarea1',
        'rows': 6
    }))

    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control',
        'id': 'exampleFormControlInput2'
    }))
