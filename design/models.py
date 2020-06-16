from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _

from parler.models import TranslatableModel, TranslatedFields
from parler.utils.context import switch_language

BUTTON_COLOR_CHOICES = (
    ('default', 'default'),
    ('primary', 'primary'),
    ('success', 'success'),
    ('info', 'info'),
    ('warning', 'warning'),
    ('danger', 'danger'),
    ('link', 'link'),
    ('disable', 'disable'),
)

BUTTON_FORM_CHOICES = (
    ('square default', ' '),
    ('square border', '-border'),
    ('radius', ' radius'),
    ('radius border', '-border radius'),
    ('circle', ' circle'),
    ('circle border ', '-border circle'),
    ('circle arrow', ' circle arrow'),
    ('circle arrow border', '-border circle arrow'),
)

BUTTON_SIZE_CHOICES = (
    ('extralarge', ' e-large'),
    ('large', ' large'),
    ('default', ' '),
    ('medium', ' medium'),
    ('small', ' small'),
)

# FONT_CHOICES = (
#     ('', ''),
#     ('', ''),
#     ('', ''),
#     ('', ''),
#     ('', ''),
#     ('', ''),
#     ('', ''),
#     ('', ''),
#     ('', ''),
#     ('', ''),
# )

#
# class DesignSettings(models.Model):

#     button_color = models.CharField(_('button_color'), max_length=100, choices=BUTTON_COLOR_CHOICES, default='default', null=True, blank=True)
#     button_size = models.CharField(_('button_size'), max_length=100, choices=BUTTON_SIZE_CHOICES, default='default', null=True, blank=True)
#     button_form = models.CharField(_('button_form'), max_length=100, choices=BUTTON_SIZE_CHOICES, default='default', null=True, blank=True)
#     fonts = models.CharField(_('fonts'), max_length=200, choices=FONT_CHOICES, default=' ', null=True, blank=True)
#     main_text_color = models.CharField(_('main_text_color (#000000 or black)'), max_length=200, default='black', null=True, blank=True)
#     main_menu_color = models.CharField(_('main_menu_color (#000000 or white)'), max_length=200, default='white', null=True, blank=True)
#     footer_color = models.CharField(_('footer_color (#000000 or white)'), max_length=200, default='white', null=True, blank=True)
#
#     class Meta:
#         verbose_name = _('Design Settings')
#         verbose_name_plural = _('Design Settings')
#
#     def __str__(self):
#         return 'DesignSettings'
#


class FunctionalSettings(models.Model):
    name = models.CharField(_('name'), blank=True, null=True, max_length=200)
    project_category = models.BooleanField(_('project_category'), default=True)
    profile_category = models.BooleanField(_('profile_category'), default=False)

    class Meta:
        verbose_name = _('Functional Settings')
        verbose_name_plural = _('Functional Settings')

    def __str__(self):
        return self.name


class PageTexts(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('name'), blank=True, null=True, max_length=200, db_index=True),
        big_page_title=RichTextUploadingField(_('big page title'), blank=True, null=True),
        small_page_title=RichTextUploadingField(_('small page title'), blank=True, null=True),
    )
    active = models.BooleanField(_('active'), default=False)

    class Meta:
        verbose_name = _('Page Texts')
        verbose_name_plural = _('Page Texts')

    def __str__(self):
        return self.name


class PagePictures(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('name'), blank=True, null=True, max_length=200, db_index=True),
    )
    image = models.ImageField(_('image'), upload_to='images/defaults/', default=None, blank=True, null=True)
    active = models.BooleanField(_('active'), default=False)

    class Meta:
        verbose_name = _('Page Pictures')
        verbose_name_plural = _('Page Pictures')

    def __str__(self):
        return self.name
