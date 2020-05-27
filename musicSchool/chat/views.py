from datetime import datetime
from django.conf import settings
from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import redirect, render
from musicSchool import settings

from django.forms.models import model_to_dict

from school.models import *
from school.forms import MessageForm
from school import views
from registration import views
from registration import form 
from django.views.generic import ListView, DetailView, CreateView



from django.views.generic.base import View

class MessageView(ListView):
    model = Message
    template_name = 'chat.html'

class ArticleDetailView(DetailView):
    model = Message
    template_name = 'chat.html'    


class AssMessageView(CreateView):
    model = Message 
    template_name = 'ind.html'
    fields = '__all__'
'''
def chat(request, pk):
    if request.method == 'GET':
        return render( request, 'chat.html',
            {
                'posts': Teacher.objects.all(),
            }
        )
    else:
        print(request.POST)
        message = Message.objects.get(id=pk)
        teacher = request.POST['teacher_name']
        text_message = request.POST.get('text_message', False)
        Message(
            date = timezone.now(),
            text_message = text_message,
            teacher = Teacher.objects.get(id=pk)
        ).save()
        return render( 
            request,
            'chat.html',
        {
        'chat': Message.objects.all()
        })

  '''
def ind(request):
    return render( request, 'ind.html')



def chatMessageAll(request):
    return render( request, 'chatMessageAll.html', {
        'chatMessageAll': MessageTest.objects.all()
    })

