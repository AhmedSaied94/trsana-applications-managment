from django import forms
from allauth.account.forms import LoginForm, SignupForm, PasswordField
from django.conf import settings
from .models import Gender


class CustomSignForm(SignupForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width:450px'}), max_length=20, required=True, label='اسم المستخدم')
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'style': 'width:450px'}), required=True, label='البريد الالكتروني')
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width:450px'}), max_length=20, required=False, label='الاسم الاول')
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width:450px'}), max_length=20, required=False, label='الاسم الاخير')

    def __init__(self, *args, **kwargs):
        super(CustomSignForm, self).__init__(*args, **kwargs)
        self.fields['phone'] = forms.CharField(widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'width:450px'}), max_length=20, required=False, label='الهاتف')
        self.fields['gender'] = forms.ChoiceField(
            widget=forms.Select(attrs={'class': 'form-control', 'style': 'width:450px'}), choices=Gender.choices, required=False, label='النوع')
        self.fields['password1'] = PasswordField(
            label='كلمة المرور', attrs={'class': 'form-control', 'style': 'width:450px'})
        self.fields['password2'] = PasswordField(label='اعد كلمة المرور', attrs={
                                                 'class': 'form-control', 'style': 'width:450px'})


class CustomLoginForm(LoginForm):
    password = PasswordField(
        label='كلمة المرور', attrs={'class': 'form-control', 'style': 'width:450px'})
    remember = forms.BooleanField(label="تذكرني", required=False)

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'] = forms.CharField(
            label='اسم المستخدم او البريد الالكتروني', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:450px'}), required=True)
