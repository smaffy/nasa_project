# Generated by Django 3.0.5 on 2020-05-04 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200504_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ind',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
