from models import Timetable
from datetime import datetime
from django.conf import settings
from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import redirect, render
from musicSchool import settings


def detail(request):
    if request.method == 'GET':
        return render( request, 'detail.html',
            {
                'posts': Timetable.objects.all(),
            }
        )
    else:
        print(request.POST)
        teacher = request.POST['name']
        text_message = request.POST.get('shirt_size', False)
        Message(
            text_message = text_message,
            teacher = Teacher.objects.get(pk=1)
        ).save()
        return render( 
            request,
            'detail.html',
        {
        'detail': Message.objects.all()
        })
