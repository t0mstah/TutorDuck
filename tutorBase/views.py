from django.shortcuts import render
from django.contrib.auth import authenticate

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