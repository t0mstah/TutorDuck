from django.shortcuts import render

# Create your views here.

from django import forms

class loginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password')

from django.shortcuts import render
from django.http import HttpResponseRedirect

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/who/')
    else:
        form = loginForm()

    return render(request, 'login.html', {'form': form})
