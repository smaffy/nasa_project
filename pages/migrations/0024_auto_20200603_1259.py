# Generated by Django 3.0.6 on 2020-06-03 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_auto_20200602_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='start_work',
            field=models.DateField(default=datetime.date(2020, 6, 3), verbose_name='start_work'),
        ),
        migrations.AlterField(
            model_name='project',
            name='completed',
            field=models.DateField(default=datetime.date(2020, 6, 3), verbose_name='completed'),
        ),
    ]
