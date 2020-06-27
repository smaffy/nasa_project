# Generated by Django 3.0.7 on 2020-06-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0042_designsettingstranslation_contact_button_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designsettings',
            name='button_form',
            field=models.CharField(blank=True, choices=[(' ', 'square default'), ('radius', 'radius'), ('circle', 'circle'), ('circle arrow', 'circle arrow')], default='radius', max_length=100, null=True, verbose_name='button_form'),
        ),
    ]
