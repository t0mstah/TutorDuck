from django import forms
from django.core.validators import RegexValidator

class userForm(forms.Form):
    email = forms.CharField(label='email', max_length=100, validators=[
        RegexValidator(regex=r'.*@stanford.edu$')
    ])
    password = forms.CharField(label='password')