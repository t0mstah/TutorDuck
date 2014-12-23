from django import forms
from django.core.validators import RegexValidator

class LoginForm(forms.Form):
    email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(label='password')

class loginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password')


class CreateForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100, validators=[
        RegexValidator(regex=r'.*@stanford.edu$', message='Not a valid email address.')
    ])
    password = forms.CharField(label='Password')
