from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from .models import *
from .forms import  CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def signup(request):   
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'User Created Successfully for ' + user)
                return redirect('loginUser')

            # context = { 'form': form }
            # return render(request, 'signup.html', context)
        context = { 'form':  CreateUserForm() }
        return render(request, 'signup.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        if request.method == 'POST':
            un = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username = un, password = passwd)
            if user is not None:
                login(request,user)
                return redirect('homePage')
            else:
                messages.info(request,'Username or password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginUser')

@login_required(login_url='loginUser')
def homePage(request):
    return render(request,'home.html')