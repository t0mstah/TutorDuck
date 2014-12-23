from tutorBase.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from tutorBase.forms import *


def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            return HttpResponseRedirect('/who/')
    else:
        form = loginForm()

    return render(request, 'login.html', {'form': form})


def create_user(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            u = User(email=email, password=password)
            u.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'create.html', {'form': form,
                                                   'error_message': 'Email must end with \'@stanford.edu\''})
    else:
        form = CreateForm()
        return render(request, 'create.html', {'form': form})

