
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', homePage, name="home"),
    path('bugBoard/', bugBoardPage, name="bugBoard"),
    path('profile/', profilePage, name="profile"),
    path('signup/', signupPage, name="signup"),
    path('login/', loginPage, name="login"),
    path('Logout/', logoffPage, name="logout"),
    path('settings/', settingPage, name='setting'),
    path('dashboard/', adminPage, name='dashboard'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)