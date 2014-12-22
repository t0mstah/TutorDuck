from django import forms
from django.core.exceptions import ValidationError


class loginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password')


class CreateForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100, validators=[validate_email()])
    password = forms.CharField(label='Password')


def validate_email(email):
    if "@stanford.edu" not in email:
        raise ValidationError('%s is not a valid email address' % email)