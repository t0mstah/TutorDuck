from django.contrib.auth import authenticate, login
from tutorBase.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from os import urandom
from base64 import b64encode


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate_user(email=email, password=password)
        if user:
            return HttpResponseRedirect(reverse('who'))
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login.'})
    else:
        return render(request, 'login.html')


def create_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        secure_bytes = urandom(50)
        char_salt = b64encode(secure_bytes).decode('utf-8')

        user = User(email=email, password=password, salt=char_salt)
        user.save()
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'create.html')


def who(request):
    return render(request, 'who.html')


def authenticate_user(email, password):
    return User.objects.filter(email=email).filter(password=password)
