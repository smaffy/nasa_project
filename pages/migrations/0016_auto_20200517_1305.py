# Generated by Django 3.0.6 on 2020-05-17 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20200515_1755'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-published'], 'verbose_name_plural': 'News'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='publicated',
            new_name='published',
        ),
    ]
