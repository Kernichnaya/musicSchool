# Generated by Django 3.0.4 on 2020-05-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0007_auto_20200526_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='surname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
