<<<<<<< HEAD
from django.shortcuts import render
from django.contrib.auth import authenticate
=======
from tutorBase.models import User
>>>>>>> 7ab576d81c3b6f5cd42fb4a8d6b9ac7e1312b7aa

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
<<<<<<< HEAD
from tutorBase.forms import LoginForm
=======
from django.core.urlresolvers import reverse
from tutorBase.forms import *

>>>>>>> 7ab576d81c3b6f5cd42fb4a8d6b9ac7e1312b7aa

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

