# Generated by Django 3.0.7 on 2020-06-13 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_customuser_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='languages',
        ),
    ]
