from django.contrib.auth import authenticate, login
from tutorBase.forms import userForm
from tutorBase.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

def login(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('who'))
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid login.'})
        else:
            return render(request, 'login.html', {'form': form, 'error_message': 'An error occurred.'})

    else:
        form = userForm()
        return render(request, 'login.html', {'form': form})

def create_user(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User(email=email, password=password)
            user.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'create.html', {'form': form, 'error_message': 'An error occurred.'})

    else:
        form = userForm()
        return render(request, 'create.html', {'form': form})

def who(request):
    return
