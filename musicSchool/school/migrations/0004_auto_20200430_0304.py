# Generated by Django 3.0.4 on 2020-04-29 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_messagetest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['teacher_name']},
        ),
    ]
