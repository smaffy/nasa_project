# Generated by Django 3.0.7 on 2020-06-20 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0024_auto_20200619_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='designsettings',
            name='overlay',
            field=models.BooleanField(default=True, verbose_name='overlay'),
        ),
        migrations.AddField(
            model_name='designsettings',
            name='overlay_color',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='overlay_color (#000000 or black)'),
        ),
        migrations.AddField(
            model_name='designsettings',
            name='overlay_opacity',
            field=models.CharField(blank=True, default=0.3, max_length=50, null=True, verbose_name='overlay_opacity (from 0.1 to 0.9)'),
        ),
    ]
