from tutorBase.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from os import urandom
from base64 import b64encode
import hashlib
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate_user(email=email, password=password)
        if user is not None:
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
        combined = (password+char_salt).encode('utf-8')

        h = hashlib.sha256(combined).hexdigest()

        user = User(email=email, password=h, salt=char_salt)
        user.save()
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'create.html')


def who(request):
    if (0 == 0):
        return render(request, 'who.html')
    else:
        return render(request, 'login.html', {'error_message': 'You must login to continue'})


def authenticate_user(email, password):

    try:
        check_user = User.objects.get(email=email)
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        return None

    combined = (password + check_user.salt).encode('utf-8')
    hash_check = hashlib.sha256(combined).hexdigest()

    try:
        found_user = User.objects.get(email=email, password=hash_check)
    except ObjectDoesNotExist:
        return None
    return found_user


def tutor(request):
    return render(request, 'tutor.html')


def student(request):
    return render(request, 'student.html')
