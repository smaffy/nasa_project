# Generated by Django 3.0.6 on 2020-05-26 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20200522_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_team',
            field=models.ManyToManyField(default=None, related_name='projects', to='pages.Profile'),
        ),
    ]
