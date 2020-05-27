from django.test import TestCase

from datetime import datetime
from django.conf import settings
from django.utils import timezone


from school.models import Teacher, Student
# Create your tests here.


class TeatModels(TestCase):

    def test_teacher(self):
        teacher1 = Teacher.objects.create(
            teacher_name = 'Иванов Владимир Иванович',
            teacher_age = '29',
            teacher_education = 'Музыкальный Колледж искусств',
            teacher_information = 'Преподаватель аккордеона и гитары' 
        )

    def test_student(self):
        student1 = Student.objects.create(
            student_name = 'Алексей',
            student_surname = 'Комаров',
            student_age = '16',
            student_phone = '+79293718254',
       )

