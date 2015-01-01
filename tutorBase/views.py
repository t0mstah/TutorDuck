from django.core.serializers import json
from tutorBase.models import User, TutorCard
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from os import urandom
from base64 import b64encode
import hashlib
import re
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.mail import send_mail


def login(request):
    if request.session.get('logged_in', False):
            return HttpResponseRedirect(reverse('who'))

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate_user(email=email, password=password)
        if user is not None:
            request.session['email'] = email
            request.session['logged_in'] = True
            return HttpResponseRedirect(reverse('who'))
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login.'})
    else:
        return render(request, 'login.html')


TEST_EMAIL = 'tommy.fang12@gmail.com'


def create_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        stanford_email = re.match('.*@stanford.edu$', email)
        if stanford_email is None:
            return render(request, 'create.html', {'error_message': 'Valid @stanford.edu email required'})

        if User.objects.filter(email=email).count() > 0:
            return render(request, 'create.html', {'error_message': 'User with email \'%s\' already exists' % email})

        if confirm != password:
            return render(request, 'create.html', {'error_message': 'Passwords do not match'})

        secure_bytes = urandom(50)
        char_salt = b64encode(secure_bytes).decode('utf-8')
        combined = (password+char_salt).encode('utf-8')

        h = hashlib.sha256(combined).hexdigest()

        request.session['email'] = email
        request.session['password'] = h
        request.session['salt'] = char_salt

        code = hashlib.sha256(urandom(20)).hexdigest()[:5].upper()
        request.session['code'] = code

        send_mail('Your verification code',
                  'Your verification code: %s\nIf you did not request this code, please ignore this message.' % code,
                  'winterproject.test@gmail.com', [TEST_EMAIL], fail_silently=False)

        return HttpResponseRedirect(reverse('verify'))
    else:
        return render(request, 'create.html')


def verify(request):
    if request.method == 'POST':
        code = request.POST['code']
        if code != request.session.get('code'):
            return render(request, 'verify.html', {'error_message': 'Incorrect Code'})

        email = request.session.get('email')
        pwd = request.session.get('password')
        salt = request.session.get('salt')

        user = User(email=email, password=pwd, salt=salt)
        user.save()
        request.session.flush()
        request.session['email'] = email
        request.session['logged_in'] = True
        return HttpResponseRedirect(reverse('who'))
    else:
        return render(request, 'verify.html')


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


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('login'), {'error_message': 'You have been logged out successfully'})


def who(request):
    if request.session.get('logged_in', False):
        return render(request, 'who.html')
    else:
        return render(request, 'login.html', {'error_message': 'You must login to continue'})


def tutor(request):
    if request.session.get('logged_in', False):
        if request.method == 'POST':
            email = request.session.get('email')
            t = User.objects.get(email=email)

            try:
                first_name = request.POST['first_name']
                school = request.POST['school']
                department = request.POST['department']
                line = request.POST['tagLine']
                description = request.POST['description']
            except KeyError:
                return render(request, 'tutor.html', {"error_message": "Some fields are empty"})

            card = TutorCard(tutor=t, first_name=first_name, school=school, department=department, tagLine=line,
                             description=description)
            card.save()
            return HttpResponseRedirect(reverse('who'))
        else:
            return render(request, 'tutor.html')
    else:
        return render(request, 'login.html', {'error_message': 'You must login to continue'})


def stanford(request, school=None, department=None, key=None):
    if request.session.get('logged_in', False):
        schools = getDepartments(school)
        if key:
            card = TutorCard.objects.get(id=key)
            return render(request, 'card.html', {'schools': schools, 'tutor': card})
        elif department:
            tutors = TutorCard.objects.filter(department=department)
            return render(request, 'department.html', {'school': school, 'schools': schools, 'tutors': tutors, 'department': department})
        elif school:
            schoolDisp = getSchoolDisp(school)
            return render(request, 'school.html', {'school': schoolDisp, 'schools': schools})
        else:
            return render(request, 'stanford.html')
    else:
        return render(request, 'login.html', {'error_message': 'You must login to continue'})


def getSchoolDisp(school):
    if school == 'engineering':
        return "Engineering"
    elif school == 'humanities':
        return "Humanities and Arts"
    elif school == 'science':
        return "Natural and Social Sciences"
    elif school == 'earth':
        return "Earth Sciences"


def getDepartments(school):
    if school == 'engineering':
        return ({'display': "Chemical Engineering", 'value': "CHE"},
               {'display': "Civil Engineering", 'value': "CE"},
               {'display': "Computer Science", 'value': "CS"},
               {'display': "Electrical Engineering", 'value': "EE"},
               {'display': "Environmental Engineering", 'value': "ENV"},
               {'display': "Management Science and Engineering", 'value': "MSAE"},
               {'display': "Materials Science and Engineering", 'value': "MSE"},
               {'display': "Mechanical Engineering", 'value': "ME"})

    elif school == 'humanities':
        return ({'display': "Art and Art History", 'value': "ART"},
               {'display': "Classics", 'value': "CLASS"},
               {'display': "English", 'value': "ENGL"},
               {'display': "History", 'value': "HIST"},
               {'display': "Linguistics", 'value': "LING"},
               {'display': "Music", 'value': "MUS"},
               {'display': "Philosophy", 'value': "PHIL"},
               {'display': "Languages", 'value': "LANG"})

    elif school == 'science':
        return ({'display': "Biology", 'value': "BIO"},
               {'display': "Chemistry", 'value': "CHEM"},
               {'display': "Communication", 'value': "COMM"},
               {'display': "Economics", 'value': "ECON"},
               {'display': "Mathematics", 'value': "MATH"},
               {'display': "Physics", 'value': "PHYS"},
               {'display': "Political Science", 'value': "POLI"},
               {'display': "Psychology", 'value': "PSYCH"},
               {'display': "Statistics", 'value': "STAT"},
               {'display': "Classics", 'value': "CLA"})

    elif school == 'earth':
        return ({'display': "Earth Systems", 'value': "ESYS"},
               {'display': "Energy Resources Engineering", 'value': "ERE"},
               {'display': "Geological and Environmental Sciences", 'value': "GES"},
               {'display': "Geophysics", 'value': "GP"})


def search_all(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        results = []

        for card in TutorCard.objects.all():
            if query in card.tutor.email or \
               query in card.first_name or \
               query in card.school or \
               query in card.department or \
               query in card.tagLine or \
               query in card.description:
                results.append(card.tagLine)

        return JsonResponse({"results": results})

    else:
        return JsonResponse({"results": ["An error has occurred."]})

