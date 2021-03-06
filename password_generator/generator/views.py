from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

# Generate Password.
# Default characters are lowercase.
# Add upper case, numbers and special characters when user checks the box.
# Use only generate to the range the user selects. 
def password(request):
    
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    char = [x.upper() for x in characters]

    if request.GET.get('uppercase'):
        characters.extend(char)

    if request.GET.get('special'):
        characters.extend(list('~!@#%^&*()_'))
    
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')