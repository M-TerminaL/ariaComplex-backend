from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator


class ActiveForm(forms.Form):
    one = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'type': 'number',
            'id': 'n1',
            'class': 'num-form d-inline',
            'maxlength': '1',

        })
    )
    two = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'type': 'number',
            'id': 'n2',
            'class': 'num-form d-inline',
            'maxlength': '1',
        })
    )
    three = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'type': 'number',
            'id': 'n3',
            'class': 'num-form d-inline',
            'maxlength': '1',
        })
    )
    four = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'type': 'number',
            'id': 'n4',
            'class': 'num-form d-inline',
            'maxlength': '1',
        })
    )
    five = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'type': 'number',
            'id': 'n5',
            'class': 'num-form d-inline',
            'maxlength': '1',
        })
    )


class LoginForm(forms.Form):
    mobile = forms.CharField(
        max_length=11,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'p-2 input-style',
            'id': 'phoneNum1',
            'type': 'tel',
            'placeholder': '09xxxxxxxxx'
        })
    )

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit():
            raise ValidationError('*فیلد موبایل باید عددی باشد')
        if not mobile.startswith('09'):
            raise ValidationError('*شماره موبایل باید با کد 09 آغاز شود')
        if len(mobile) != 11:
            raise ValidationError('*شماره موبایل باید 11 رقمی باشد')

        return mobile


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=25,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'p-2 input-style',
            'id': 'name',
            'type': 'text',
            'placeholder': 'مثال : علیرضا'
        }),
        validators=[MaxLengthValidator(20),
                    RegexValidator(regex=r'[\u0621-\u06cc\u00ab\u00bb\u060c\u061b]+',
                                   message='*نام خود را به درستی وارد نمایید')
                    ]
    )
    last_name = forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'p-2 input-style',
            'id': 'lname',
            'type': 'text',
            'placeholder': 'مثال : کلانتری'
        }),
        validators=[MaxLengthValidator(50),
                    RegexValidator(regex=r'[\u0621-\u06cc\u00ab\u00bb\u060c\u061b]+',
                                   message='*نام خانوادگی خود را به درستی وارد نمایید')
                    ]
    )
    mobile = forms.CharField(
        max_length=11,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'p-2 input-style',
            'id': 'phoneNum1',
            'type': 'tel',
            'placeholder': '09xxxxxxxxx'
        })
    )

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit():
            raise ValidationError('*فیلد موبایل باید عددی باشد')
        if not mobile.startswith('09'):
            raise ValidationError('*شماره موبایل باید با کد 09 آغاز شود')
        if len(mobile) != 11:
            raise ValidationError('*شماره موبایل باید 11 رقمی باشد')

        return mobile


class LoginPassVerifyForm(forms.Form):
    one = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'type': 'number',
            'id': 'n1',
            'class': 'num-form d-inline',
            'maxlength': '1',
        })
    )
    two = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'type': 'number',
            'id': 'n2',
            'class': 'num-form d-inline',
            'maxlength': '1',
        })
    )
    three = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'type': 'number',
            'id': 'n3',
            'class': 'num-form d-inline',
            'maxlength': '1',
        })
    )
    four = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'type': 'number',
            'id': 'n4',
            'class': 'num-form d-inline',
            'maxlength': '1',
        })
    )
    five = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'type': 'number',
            'id': 'n5',
            'class': 'num-form d-inline',
            'maxlength': '1',
        })
    )
