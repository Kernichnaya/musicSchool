from django.contrib import admin

# Register your models here.

from .models import Teacher, Message, Student
#from chat.models import Message

admin.site.register(Teacher)
admin.site.register(Message)
admin.site.register(Student)
