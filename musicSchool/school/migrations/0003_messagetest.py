# Generated by Django 3.0.4 on 2020-04-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('text', models.CharField(max_length=500)),
            ],
        ),
    ]