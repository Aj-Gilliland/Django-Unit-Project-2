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
    # except:
    #     print('Error, loading bugBoardPage in Safe mode')
    #     fakeObject = {
    #     'title': "Uhhh python broke",
    #     'content':  'Erm the computer is on fire and i dont know what to do. Honestly I think im about to give up, please help.',
    #     'messages': ['msg1','msg2','msg3'],
    #     'winner': 'Adrian'
    #     }
    #     fakeObject2 = {
    #     'title': "Uhhh python broke again",
    #     'content':  'Erm the computer is on fire and i dont know what to do. Honestly I think im about to give up, please help...again.',
    #     'messages': ['this is a message that is slightly long','i assure you that this will be a long message, in fact so big that you might want to stop reading soon enough.','I guess I could make this a medium message, so like five more words?','Last but not least this is just going to be a message, of no importance. Why are you still reading?'],
    #     'winner': ''
    #     }
    #     context = {'bugReports':[fakeObject,fakeObject2,fakeObject,fakeObject2,fakeObject,fakeObject2,fakeObject,fakeObject2,fakeObject,fakeObject2,fakeObject,fakeObject2]}
    #     return render(request, "bugBoard.html", context)

@login_required(login_url='login')
def profilePage(request:HttpRequest)->HttpResponse:
    # try:
        account = getAccountFor(request.user)
        tokenGraphData = getBugsSolvedPerMonth(account)
        reportList = getUserBugReports(request.user)
        notificationList = getNotificationsFor(request.user)
        context = {'notificationList':notificationList,'totalTokenList':tokenGraphData,'userBugReports':reportList,'profile_pic':account.profile_picture,'notifications':['These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days'],'awardeList':['uPVoted by Jordan 2/13/24','upvote by Aj 1/2/24','upvote by Adrian 1/1/24''upvote by Joe 2/13/24',"Your comment received credit for fixing Mathew's bug",'upvote by Jordan 2/13/24','upvote by Aj 1/2/24','upvote by Adrian 1/1/24''upvote by Joe 2/13/24',"Your comment received credit for fixing Mathew's bug"]}
        return render(request, "profile.html", context)
    # except:
    #     print('Loading profile page in safe mode')
    #     context = {'totalTokenList':[12,33,3,25,31,59,2],'notifications':['These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days','These are test notifactions','leave notifiactions in a list in context','erm ur bug hasnt been solved in two days'],'userBugReports':['These are test reports','these would be reports that you put out','erm ur bug hasnt been solved in two days','These are test reports','these would be reports that you put out','erm ur bug hasnt been solved in two days'],'awardeList':['upvote by Jordan 2/13/24','upvote by Aj 1/2/24','upvote by Adrian 1/1/24''upvote by Joe 2/13/24',"Your comment received credit for fixing Mathew's bug",'upvote by Jordan 2/13/24','upvote by Aj 1/2/24','upvote by Adrian 1/1/24''upvote by Joe 2/13/24',"Your comment received credit for fixing Mathew's bug"]}
    #     return render(request, "profile.html", context)
    
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
    account = getAccountFor(request.user)
    context = {'account':account, 'form': form}
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
