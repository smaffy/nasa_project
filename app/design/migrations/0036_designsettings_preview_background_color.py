# Generated by Django 3.0.7 on 2020-06-26 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0035_designsettings_footer_background_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='designsettings',
            name='preview_background_color',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='preview_background_color'),
        ),
    ]
