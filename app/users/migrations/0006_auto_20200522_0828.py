# Generated by Django 3.0.6 on 2020-05-22 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]