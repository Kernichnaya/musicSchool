<<<<<<< HEAD
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
		return redirect('/school')#
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
		return redirect('/school')#
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/school')#
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')
=======
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserChangeForm

def registration(response):
    form = UserChangeForm()
    return render(response, 'registration/registration.html', {'form':form})
>>>>>>> 9fd7f1660f677d3310da13082a0324890bdebbf6
