# Generated by Django 3.0.7 on 2020-06-16 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0006_pagetextstranslation_banner_big_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetexts',
            name='add_name',
            field=models.BooleanField(default=False, verbose_name='add_name_to_bannertext'),
        ),
    ]