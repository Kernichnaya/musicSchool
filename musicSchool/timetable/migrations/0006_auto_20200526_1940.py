# Generated by Django 3.0.4 on 2020-05-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_auto_20200526_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Понедельник', (('10:00', '10:00'), ('12:00', '12:00'), ('15:00', '15:00'), ('17:00', '17:00'))), ('Вторник', (('10:00', '10:00'), ('12:00', '12:00'), ('15:00', '15:00'), ('17:00', '17:00'))), ('Среда', (('10:00', '10:00'), ('12:00', '12:00'), ('15:00', '15:00'), ('17:00', '17:00'))), ('Четверг', (('10:00', '10:00'), ('12:00', '12:00'), ('15:00', '15:00'), ('17:00', '17:00'))), ('Пятница', (('10:00', '10:00'), ('12:00', '12:00'), ('15:00', '15:00'), ('17:00', '17:00')))], max_length=200, null=True),
        ),
    ]
