from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import models, forms

#register
def register_view(request):
    if request.method == "POST":
        form = forms.CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = forms.CustomRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#login
def auth_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/user_list/')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
    
#logout
def auth_logout_view(request):
    logout(request)
    return redirect('/login/')



#user_list
def user_list_view(request):
    if request.method == "GET":
        user_list = models.CustomUser.objects.all()
    return render(request, 'users/user_list.html', {'us': user_list})