from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse

def homePage(request:HttpRequest)->render:
    context = {}
    return render(request, "home.html", context)

def communityPage(request:HttpRequest)->render:
    context = {}
    return render(request, "community.html", context)

def documentationPage(request:HttpRequest)->render:
    context = {}
    return render(request, "documentation.html", context)

def managementPage(request:HttpRequest)->render:
    context = {}
    return render(request, "management.html", context)

def procurementPage(request:HttpRequest)->render:
    context = {}
    return render(request, "procurement.html", context)