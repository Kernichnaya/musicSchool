# Generated by Django 3.0.4 on 2020-05-26 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_delete_timetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_surname',
        ),
    ]