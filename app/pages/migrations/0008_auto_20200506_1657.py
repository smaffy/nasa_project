# Generated by Django 3.0.6 on 2020-05-06 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20200505_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='category_slug',
        ),
    ]
