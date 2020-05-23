import datetime

from django.db import models
from django.utils import timezone


class Timetable(models.Model):
    SHIRT_SIZES = [
    ('Понедельник', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )
    ),
    ('Вторник', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )
    ),
    ('Среда', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )
    ),   
    ('Четверг', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )
    ),  
    ('Пятница', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )),
]

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=5, choices=SHIRT_SIZES) 



class TimetablСhoice(models.Model):
    date = models.DateTimeField()
    name_student = models.CharField(max_length=500)
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE) 