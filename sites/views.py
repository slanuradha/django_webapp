from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sites.forms import UserLoginForm


def registration(request):

    form = UserCreationForm()
    message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = User()
            user.username = username
            user.set_password(password)
            user.save()
            message = 'User: '+ username + 'registered successfully'

    return render(request, 'site/registration.html', {'form': form, 'msg': message})


def logIn(request):

    if request.user.username:
        return redirect(dashboard)

    form = UserLoginForm()
    message = ''
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is None:
                message = 'Invalid login details!'
            else:
                login(request, user)
                request.session['city'] = 'Bangalore'
                request.session['address'] = 'BTM'
                return redirect(dashboard)

    return render(request, 'site/login.html', {'form': form, 'msg': message})


def dashboard(request):
    return render(request, 'site/dashboard.html')
def logoutUser(request):
    logout(request)
    return redirect(login)
