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
from datetime import datetime
 
def homePage(request:HttpRequest)->HttpResponse:
    if request.user.is_authenticated:
        return redirect('bugBoard')
    else:
        context = {}
        return render(request, "home.html", context)

def bugBoardPage(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        report_form = ReportForm(request.POST)
        if report_form.is_valid():
            title = report_form.cleaned_data['title']
            prompt = report_form.cleaned_data['prompt']
            user = request.user
            makeReport(user,prompt,title)
    else:
        report_form = ReportForm()
    reportList = getAllReports()
    context = {'bugReports': reportList, 'report_form': report_form,}
    return render(request, "bugBoard.html", context)

@login_required(login_url='login')
def profilePage(request:HttpRequest)->HttpResponse:
    account = getAccountFor(request.user)
    tokenGraphData = getBugsSolvedPerMonth(account)
    reportList = getUserBugReports(request.user)
    notificationList = getNotificationsFor(request.user)
    context = {'notificationList':notificationList,'totalTokenList':tokenGraphData,'userBugReports':reportList,'profile_pic':account.profile_picture,'notifications':['These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days'],'awardeList':['uPVoted by Jordan 2/13/24','upvote by Aj 1/2/24','upvote by Adrian 1/1/24''upvote by Joe 2/13/24',"Your comment received credit for fixing Mathew's bug",'upvote by Jordan 2/13/24','upvote by Aj 1/2/24','upvote by Adrian 1/1/24''upvote by Joe 2/13/24',"Your comment received credit for fixing Mathew's bug"]}
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
                #vvvvvvv   this associates a user with an account if they are not already 
                if hasAccount(user):
                    return redirect('home')
                else:
                    makeAccount(user)
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
    password_change_form = None  
    picture_change_form = None
    if request.method == 'POST':
        #checks for password change form
        if 'password_change_submit' in request.POST:
            password_change_form = PasswordChangeForm(request.user, request.POST)
            if password_change_form.is_valid():
                print('ready to change')
                user = password_change_form.save()
                update_session_auth_hash(request, user)
                return redirect('setting')
            else:
                for field, errors in password_change_form.errors.items():
                    for error in errors:
                        messages.error(request, f"Error in {field}: {error}")
                print(f'The password change form was not completed correctly: {password_change_form.errors}')
        #checks for photo change form
        elif 'picture_change_submit' in request.POST:
            picture_change_form = pfpChangeForm(request.POST, request.FILES)
            if picture_change_form.is_valid():
                clean_picture = picture_change_form.cleaned_data['picture']
                changePfp(request.user,clean_picture)
                return redirect('setting')
            else:
                messages.error(request, 'Error updating profile picture.')
                print(f'The profile picture change form was not completed correctly: {picture_change_form.errors}')
    else:
        password_change_form = PasswordChangeForm(request.user)
        picture_change_form = pfpChangeForm()
    account = getAccountFor(request.user)
    context = {'account': account, 'password_change_form': password_change_form, 'picture_change_form': picture_change_form}
    return render(request, 'setting.html', context)


@staff_member_required
def adminPage(request: HttpRequest) -> HttpResponse:
    print(f'Current User id: {request.user.id}')
    if request.method == 'POST':
        form = adminDeleteForm(request.POST)  
        if form.is_valid():
            type_value = form.cleaned_data['type']
            index_value = form.cleaned_data['index']
            deleteResponse = adminDelete(type_value, index_value)
            context = {'form': form, 'deleteResponse': deleteResponse}
            return render(request, 'admin.html', context)
    else:
        form = adminDeleteForm()

    context = {'form': form}
    return render(request, 'admin.html', context)
