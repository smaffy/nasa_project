# Generated by Django 3.0.7 on 2020-06-19 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0023_auto_20200619_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='designsettings',
            name='banner_height',
            field=models.CharField(blank=True, default=350, max_length=50, null=True, verbose_name='banner_height'),
        ),
        migrations.AddField(
            model_name='designsettings',
            name='home_banner_height',
            field=models.CharField(blank=True, default=950, max_length=50, null=True, verbose_name='home_banner_height'),
        ),
    ]
