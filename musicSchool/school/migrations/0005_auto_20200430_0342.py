# Generated by Django 3.0.4 on 2020-04-29 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20200430_0304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='text',
            new_name='text_message',
        ),
    ]