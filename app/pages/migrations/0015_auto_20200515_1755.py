# Generated by Django 3.0.6 on 2020-05-15 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20200515_1317'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-completed'], 'verbose_name_plural': 'Projects'},
        ),
    ]