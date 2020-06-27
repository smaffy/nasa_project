# Generated by Django 3.0.7 on 2020-06-26 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0038_designsettings_footer_font_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designsettings',
            name='button_color',
            field=models.CharField(blank=True, choices=[('default', 'default'), ('default-border', 'default-border'), ('primary', 'primary'), ('primary-border', 'primary-border'), ('success', 'success'), ('success-border', 'success-border'), ('info', 'info'), ('info-border', 'info-border'), ('warning', 'warning'), ('warning-border', 'warning-border'), ('danger', 'danger'), ('danger-border', 'danger-border'), ('link', 'link'), ('link-border', 'link-border'), ('disable', 'disable'), ('disable-border', 'disable-border')], default='success', max_length=100, null=True, verbose_name='button_color'),
        ),
        migrations.AlterField(
            model_name='designsettings',
            name='button_form',
            field=models.CharField(blank=True, choices=[('', 'square default'), ('radius', 'radius'), ('circle', 'circle'), ('circle arrow', 'circle arrow')], default=' radius', max_length=100, null=True, verbose_name='button_form'),
        ),
    ]