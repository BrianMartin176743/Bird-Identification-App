# Generated by Django 3.1.4 on 2020-12-03 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
