# Generated by Django 3.0.6 on 2020-06-04 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetextstranslation',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True, verbose_name='name'),
        ),
    ]