# Generated by Django 3.0.6 on 2020-06-05 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_auto_20200605_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(default='/images/defaults/project-details.jpg', upload_to='images/projects/', verbose_name='project image'),
        ),
    ]