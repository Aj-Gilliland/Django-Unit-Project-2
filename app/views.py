from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse

def homePage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "home.html", context)

def communityPage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "community.html", context)

def documentationPage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "documentation.html", context)

def managementPage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "management.html", context)

def procurementPage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "procurement.html", context)

def signupPage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "signup.html", context)

def loginPage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "login.html", context)