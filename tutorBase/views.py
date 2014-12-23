from django.contrib.auth import authenticate
from tutorBase.forms import CreateForm
from tutorBase.models import User
from django.core.urlresolvers import reverse

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from tutorBase.forms import LoginForm

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user:
            return HttpResponseRedirect('/who/')
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
            return render(request, 'create.html', {'form':form})

    else:
        form = CreateForm()
        return render(request, 'create.html', {'form': form})

