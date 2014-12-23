from django.contrib.auth import authenticate
from tutorBase.forms import CreateForm
from tutorBase.forms import LoginForm
from tutorBase.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

def login(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user:
            return HttpResponseRedirect('/who')

    else:
        form = LoginForm()

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
            return render(request, 'create.html', {'form': form, 'error_message': 'An error occurred.'})

    else:
        form = CreateForm()
        return render(request, 'create.html', {'form': form})
