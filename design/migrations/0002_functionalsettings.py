# Generated by Django 3.0.7 on 2020-06-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionalSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_category', models.BooleanField(default=True, verbose_name='project_category')),
                ('profile_category', models.BooleanField(default=False, verbose_name='profile_category')),
            ],
            options={
                'verbose_name': 'Functional Settings',
                'verbose_name_plural': 'Functional Settings',
            },
        ),
    ]