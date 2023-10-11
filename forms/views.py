# person/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
# from .models import forms

people = []  # List to store Person instances

class forms:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_person = forms(username, password)
        people.append(new_person)
        return HttpResponseRedirect('/')

    return render(request, 'add.html')

def show(request):
    return render(request, 'show.html', {'people': people})
