from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from .models import *
from .forms import UserForm, CreateUserForm


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'User Created Successfully for' + user)
            return redirect('login/')

    context = { 'form': form}
    return render(request, 'signup.html', context)


def login(request):
    return render(request, 'login.html')
