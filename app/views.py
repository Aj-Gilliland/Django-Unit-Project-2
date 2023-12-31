from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import password_validation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


def homePage(request:HttpRequest)->HttpResponse:
    if request.user.is_authenticated:
        return redirect('bugBoard')
    else:
        context = {}
        return render(request, "home.html", context)

@login_required(login_url='login')
def bugBoardPage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "bugBoard.html", context)

@login_required(login_url='login')
def profilePage(request:HttpRequest)->HttpResponse:
    context = {'totalTokenList':[12,33,3,25,31,59,2],'notifications':['These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days'],'userBugReports':['These are test reports','these would be reports that you put out','erm ur bug hasnt been solved in two days','These are test reports','these would be reports that you put out','erm ur bug hasnt been solved in two days'],'awardeList':['upvote by Jordan 2/13/24','upvote by Aj 1/2/24','upvote by Adrian 1/1/24''upvote by Joe 2/13/24',"Your comment received credit for fixing Mathew's bug",'upvote by Jordan 2/13/24','upvote by Aj 1/2/24','upvote by Adrian 1/1/24''upvote by Joe 2/13/24',"Your comment received credit for fixing Mathew's bug"]}
    return render(request, "profile.html", context)

def signupPage(request:HttpRequest)->HttpResponse:
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                errors = form.errors.values()
                context = {'form': form, 'errors': errors}
                return render(request, "signup.html", context)
        context = {'form':form,'errors':[]}
        return render(request, "signup.html",context)

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

def logoffPage(request:HttpRequest)->HttpResponse:
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def settingPage(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('setting')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            print(f'The form was not completed correctly: {form.errors}')  
    else:
        form = PasswordChangeForm(request.user)

    context = {'form': form}
    return render(request, 'setting.html', context)