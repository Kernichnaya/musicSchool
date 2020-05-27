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

def ind(request):
    return render( request, 'ind.html')


