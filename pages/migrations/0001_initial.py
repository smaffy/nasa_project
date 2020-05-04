# Generated by Django 3.0.5 on 2020-05-03 14:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('short_description', models.TextField()),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='images/defaults/news.jpg', upload_to='images/news/')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, unique=True)),
                ('last_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('start_work', models.DateField()),
                ('short_description', models.TextField()),
                ('image', models.ImageField(default='images/defaults/project-details.jpg', upload_to='images/news/')),
            ],
            options={
                'verbose_name_plural': 'Profiles',
                'ordering': ['start_work'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('client', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('completed', models.DateField()),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(default='images/defaults/project-details.jpg', upload_to='images/projects/')),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ['completed'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
    ]
