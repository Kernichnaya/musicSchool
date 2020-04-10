from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserChangeForm

def registration(response):
    form = UserChangeForm()
    return render(response, 'registration/registration.html', {'form':form})
