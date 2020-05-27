from django.db import models

from django.forms import ModelForm
from registration.form import CreateUserForm
from django.contrib.auth.models import User
from django.forms import ModelForm 
from django.urls import reverse

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    teacher_age = models.CharField(max_length=50)
    teacher_education = models.CharField(max_length=300)
    teacher_information = models.CharField(max_length=600)
    
    class Meta:

        ordering =['teacher_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('teacher-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.teacher_name)


class Student(models.Model):
    student_name = models.CharField(max_length=30)
    student_surname = models.CharField(max_length=30)
    student_age = models.CharField(max_length=50)
    student_phone = models.CharField(max_length=15)


class Message(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=50)
    def __str__(self):
		    return self.title + ' | ' + str(self.author)
    def get_absolute_url (self):
        return reverse('ind')

class MessageTest(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    text = models.CharField(max_length=500)

