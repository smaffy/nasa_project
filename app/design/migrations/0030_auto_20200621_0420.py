# Generated by Django 3.0.7 on 2020-06-21 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0029_auto_20200621_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designsettings',
            name='banner_height',
            field=models.CharField(blank=True, default=300, max_length=50, null=True, verbose_name='banner_height'),
        ),
    ]