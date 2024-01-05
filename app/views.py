from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def homePage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "home.html", context)

@login_required(login_url='login')
def communityPage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "community.html", context)

@login_required(login_url='login')
def documentationPage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "documentation.html", context)

@login_required(login_url='login')
def managementPage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "management.html", context)

@login_required(login_url='login')
def procurementPage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "procurement.html", context)

def signupPage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "signup.html", context)

def loginPage(request:HttpRequest)->HttpResponse:
    if request.user.is_authenticated:
            return redirect('home')
    else:
        if request.method == 'POST' :
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context = {'Incorrect_username_or_password':'Incorrect username or password'}
                return render (request, 'login.html', context)
    context = {}
    return render (request, 'login.html', context)