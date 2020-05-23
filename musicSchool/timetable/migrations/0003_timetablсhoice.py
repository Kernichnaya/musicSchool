# Generated by Django 3.0.4 on 2020-05-14 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20200515_0345'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimetablСhoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('name_student', models.CharField(max_length=500)),
                ('timetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Timetable')),
            ],
        ),
    ]
