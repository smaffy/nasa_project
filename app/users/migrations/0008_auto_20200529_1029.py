# Generated by Django 3.0.6 on 2020-05-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200529_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='registation_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='registation_number'),
        ),
    ]
