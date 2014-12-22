from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from tutorBase.forms import loginForm

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/who/')
    else:
        form = loginForm()

    return render(request, 'login.html', {'form': form})