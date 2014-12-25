from tutorBase.models import User, TutorCard
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from os import urandom
from base64 import b64encode
import hashlib
import re
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

        stanford_email = re.match('.*@stanford.edu$', email)
        if stanford_email is None:
            return render(request, 'create.html', {'error_message': 'Valid @stanford.edu email required'})

        if User.objects.filter(email=email).count() > 0:
            return render(request, 'create.html', {'error_message': 'User with email \'%s\' already exists' % email})

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
    if 0 == 0:
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
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        return None
    return found_user


def tutor(request):
    if request.method == 'POST':
        tutor = User.objects.get(id=1)
        first_name = request.POST['first_name']
        school = request.POST['school']
        department = request.POST['department']
        tagLine = request.POST['tagLine']
        description = request.POST['description']

        tutorCard = TutorCard(tutor=tutor, first_name=first_name, school=school, department=department, tagLine=tagLine, description=description)
        tutorCard.save()
        return render(request, 'who.html')
    else:
        return render(request, 'tutor.html')


def school(request):
    return render(request, 'school.html')

def engineering(request):
    return render(request, 'engineering.html')

def humanities(request):
    return render(request, 'humanities.html')

def science(request):
    return render(request, 'science.html')

def earth(request):
    return render(request, 'earth.html')