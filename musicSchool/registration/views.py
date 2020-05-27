from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .form import CreateUserForm


def registrationPage(request):
	if request.user.is_authenticated:
		return redirect('/')#
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')#
			

		context = {'form':form}
		return render(request, 'registration/registration.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/timetable/')#
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/timetable/')#
			else:
				messages.info(request, 'Неверный логин или пароль')

		context = {}
		return render(request, 'login/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('/')
