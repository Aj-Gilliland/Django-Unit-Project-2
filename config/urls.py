
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [

    path('admin/', admin.site.urls, name="admin"),

    path('home/', homePage, name="home"),

    path('community/', communityPage, name="community"),
    path('documentation/', documentationPage, name="documentation"),
    path('management/', managementPage, name="management"),
    path('procurement/', procurementPage, name="procurement"),
    
]
