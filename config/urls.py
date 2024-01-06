
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', homePage, name="home"),
    path('bugBoard/', bugBoardPage, name="bugBoard"),
    path('profile/', profilePage, name="profile"),
    # path('community/', communityPage, name="community"),
    # path('documentation/', documentationPage, name="documentation"),
    # path('management/', managementPage, name="management"),
    # path('procurement/', procurementPage, name="procurement"),
    path('signup/', signupPage, name="signup"),
    path('login/', loginPage, name="login"),
    path('Logout/', logoffPage, name="logout"),
]
