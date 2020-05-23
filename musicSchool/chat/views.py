from datetime import datetime
from django.conf import settings
from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import redirect, render
from musicSchool import settings

from django.forms.models import model_to_dict

from school.models import Teacher, Message, MessageTest

from school import views
from registration import views
from registration import form




from django.views.generic.base import View


def chat(request):
    if request.method == 'GET':
        return render( request, 'chat.html',
            {
                'posts': Teacher.objects.all(),
            }
        )
    else:
        print(request.POST)
        teacher = request.POST['teacher_name']
        text_message = request.POST.get('text_message', False)
        Message(
            date = timezone.now(),
            text_message = text_message,
            teacher = Teacher.objects.get(id=2)
        ).save()
        return render( 
            request,
            'chat.html',
        {
        'chat': Message.objects.all()
        })


        
def ind(request):
    return render( request, 'ind.html')



'''
def chatMessage(request, number):
    mes = MessageTest.objects.filter(id=number)######

    if len(mes) == 1:
        mess = model_to_dict(mes[0])
        return render( request, 'chatMessage.html', mess)
    else:
         return redirect('/ind')


def chatInput(request):
    if request.method == 'GET':
        return render(request, 'chatInput.html')
    else:
        secret = request.POST['secret']
        name = request.POST['name']
        text = request.POST['text']

        if secret != settings.SECRET_KEY:
            return render(request, 'chatInput.html', {
                'error': 'Неправильный SECRET KEY'
            })
        if len(name) == 0:
            return render(request, 'chatInput.html', {
                'error': 'Пустое имя'
            })            
        if len(text) == 0:
            return render(request, 'chatInput.html', {
                'error': 'Пустой text'
            }) 


        MessageTest(
            name=name, 
            date=datetime.now(),
            text=text,
        ).save()
        return redirect('/chatMessageAll/')

'''


def chatMessageAll(request):
    return render( request, 'chatMessageAll.html', {
        'chatMessageAll': MessageTest.objects.all()
    })





'''
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render
from musicSchool import settings

from django.forms.models import model_to_dict

from school.models import Teacher
from school import views
from registration import views
from registration import form
from chat.models import Message



from django.views.generic.base import View


def chat(request):
    if request.method == 'GET':
        return render( request, 'chat.html',
            {
                'posts': Teacher.objects.all(),
            }
        )
    else:
            print(request.POST)
            results=request.POST['teacher_name']
            return render( request, 'chat.html', {'teacher_name': results})


        
def ind(request):
    return render( request, 'ind.html')




def chatMessage(request, number):
    mes = Message.objects.filter(id=number)

    if len(mes) == 1:
        mess = model_to_dict(mes[0])
        return render( request, 'chatMessage.html', mess)
    else:
         return redirect('/ind')


def chatInput(request):
    if request.method == 'GET':
        return render(request, 'chatInput.html')
    else:
        secret = request.POST['secret']
        name = request.POST['name']
        text = request.POST['text']

        if secret != settings.SECRET_KEY:
            return render(request, 'chatInput.html', {
                'error': 'Неправильный SECRET KEY'
            })
        if len(name) == 0:
            return render(request, 'chatInput.html', {
                'error': 'Пустое имя'
            })            
        if len(text) == 0:
            return render(request, 'chatInput.html', {
                'error': 'Пустой text'
            }) 


        Message(
            name=name, 
            date=datetime.now(),
            text=text,
        ).save()
        return redirect('/chatMessageAll/')

def chatMessageAll(request):
    return render( request, 'chatMessageAll.html', {
        'chatMessageAll': Message.objects.all()
    })


'''