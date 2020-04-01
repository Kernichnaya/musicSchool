from django.db import models

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    teacher_age = models.CharField(max_length=50)
    teacher_education = models.CharField(max_length=300)
    teacher_information = models.CharField(max_length=600)
    
#    object = models.manager()
    
    def __str__(self):
        return self.teacher_name