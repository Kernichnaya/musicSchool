# Generated by Django 3.0.4 on 2020-05-26 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0013_auto_20200526_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='message',
            name='text_message',
        ),
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='body',
            field=models.CharField(default=11, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
