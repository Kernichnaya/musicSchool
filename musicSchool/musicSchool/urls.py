"""musicSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from registration import views as v
<<<<<<< HEAD
from chat import views as views

urlpatterns = [
    path('school', include('school.urls')),
    path('chat', views.chat, name='chat'),
    path('ind', views.ind, name='ind'),
#    path('chatMessage/<int:number>', views.chatMessage, name='chatMessage'),
    path('chatMessageAll', views.chatMessageAll, name='chatMessageAll'),    
#    path('chatInput', views.chatInput, name='chatInput'),

    path('registration/', v.registrationPage, name='registration'),
    path('login/', v.loginPage, name='login'),
=======

urlpatterns = [
    path('school/', include('school.urls')),
    path('registration/', v.registration, name='registration'),  
>>>>>>> 9fd7f1660f677d3310da13082a0324890bdebbf6
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

#    path('timetable/', include('timetable.urls')),
]