# Generated by Django 3.0.6 on 2020-06-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_auto_20200603_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_category',
            field=models.ManyToManyField(blank=True, default=None, related_name='profile_category', to='pages.ProfileCategory'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_category',
            field=models.ManyToManyField(blank=True, default=None, related_name='project_category', to='pages.ProjectCategory'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_team',
            field=models.ManyToManyField(blank=True, default=None, related_name='projects', to='pages.Profile'),
        ),
    ]
