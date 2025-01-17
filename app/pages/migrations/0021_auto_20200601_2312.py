# Generated by Django 3.0.6 on 2020-06-01 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_auto_20200528_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcategory',
            name='category_slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='category_slug'),
        ),
        migrations.AlterField(
            model_name='projectcategory',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='title'),
        ),
    ]
