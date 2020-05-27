from django.shortcuts import render

from .models import Teacher
from django.contrib.auth import authenticate



def index(request):
    return render(
        request, 
        'index.html',
        {
            'posts': Teacher.objects.all(),
        }    
    )
