# Generated by Django 3.0.4 on 2020-04-26 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0006_delete_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('text', models.CharField(max_length=500)),
            ],
        ),
    ]
