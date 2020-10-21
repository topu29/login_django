from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import UserForm, CreateUserForm


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = { 'form': form}
    return render(request, 'signup.html', context)


def login(request):
    return render(request, 'login.html')
