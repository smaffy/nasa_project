# Generated by Django 3.0.7 on 2020-06-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0039_auto_20200626_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designsettings',
            name='button_form',
            field=models.CharField(blank=True, choices=[(' ', 'square default'), ('radius', 'radius'), ('circle', 'circle'), ('circle arrow', 'circle arrow')], default=' radius', max_length=100, null=True, verbose_name='button_form'),
        ),
    ]
