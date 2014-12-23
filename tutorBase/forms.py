from django import forms
from django.core.validators import RegexValidator

<<<<<<< HEAD
class LoginForm(forms.Form):
    email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(label='password')
=======
class loginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password')


class CreateForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100, validators=[
        RegexValidator(regex=r'.*@stanford.edu$', message='Not a valid email address.')
    ])
    password = forms.CharField(label='Password')
>>>>>>> 7ab576d81c3b6f5cd42fb4a8d6b9ac7e1312b7aa
