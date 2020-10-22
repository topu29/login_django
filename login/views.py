from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from .models import *
from .forms import UserForm, CreateUserForm
from django.contrib.auth import authenticate,login,logout

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'User Created Successfully for' + user)
            return redirect('login')

    context = { 'form': form }
    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(request, username = un, password = passwd)
        if user is not None:
            login(user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)
