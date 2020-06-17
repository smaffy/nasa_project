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
    (' ', 'square default'),
    ('-border', 'square border'),
    (' radius', 'radius'),
    ('-border radius', 'radius border'),
    (' circle', 'circle'),
    ('-border circle', 'circle border'),
    (' circle arrow', 'circle arrow'),
    ('-border circle arrow', 'circle arrow border'),
)

BUTTON_SIZE_CHOICES = (
    (' e-large', 'extralarge'),
    (' large', 'large'),
    (' ', 'default'),
    (' medium', 'medium'),
    (' small', 'small'),
)

HOME = (
    ('left', 'left'),
    ('center', 'center'),
    ('right', 'right'),
)

FONT_CHOICES = (
    ("Poppins, sans-serif", "default"),
    ("Sriracha, cursive", "Sriracha"),
    ("Lato, sans-serif", "Lato"),
    ("Roboto, sans-serif", "Roboto"),
    ("Open Sans, sans-serif", "Open Sans"),
    ("Caveat, cursive", "Caveat"),
    ("Yanone Kaffeesatz, sans-serif", "Yanone Kaffeesatz"),
    ("Inconsolata, monospace", "Inconsolata"),
    ("Rubik, sans-serif", "Rubik"),
    ("Merriweather, serif", "Merriweather"),
    ("Arizonia, cursive", "Arizonia"),
    ("Permanent Marker, cursive", "Permanent Marker"),
    ("Marck Script, cursive", "Marck Script"),
)


class DesignSettings(TranslatableModel):
    translations = TranslatedFields(
        home_big_banner_button=models.CharField(_('home_big_banner_button'), max_length=50, default='', null=True, blank=True)
    )
    name = models.CharField(_('name'), default='design', blank=True, null=True, max_length=200, editable=False)
    info = models.CharField(_('info'), blank=True, null=True, max_length=200)

    button_color = models.CharField(_('button_color'), max_length=100, choices=BUTTON_COLOR_CHOICES, default='success', null=True, blank=True)
    button_size = models.CharField(_('button_size'), max_length=100, choices=BUTTON_SIZE_CHOICES, default=' ', null=True, blank=True)
    button_form = models.CharField(_('button_form'), max_length=100, choices=BUTTON_FORM_CHOICES, default=' radius', null=True, blank=True)
    home_banner_text_align = models.CharField(_('home_banner_text_align'), max_length=100, choices=HOME, default='center', null=True, blank=True)
    font = models.CharField(_('fonts'), max_length=200, choices=FONT_CHOICES, default='default', null=True, blank=True)

    main_text_color = models.CharField(_('main_text_color (#000000 or black)'), max_length=200, default='black', null=True, blank=True)
    main_menu_text_color = models.CharField(_('main_menu_color (#000000 or white)'), max_length=200, default='black', null=True, blank=True)
    background_color = models.CharField(_('main_text_color (#000000 or black)'), max_length=200, default='lightgray', null=True, blank=True)
    container_color = models.CharField(_('main_text_color (#000000 or black)'), max_length=200, default='white', null=True, blank=True)
    vertical_lines_color = models.CharField(_('main_text_color (#000000 or black)'), max_length=200, default='gray', null=True, blank=True)

    background_image = models.ImageField(_('background_image'), upload_to='images/background/', default=None, blank=True, null=True)

    background_image_on = models.BooleanField(_('background_image_on'), default=False)
    full_top_banner = models.BooleanField(_('full_top_banner'), default=True)
    menu_left = models.BooleanField(_('menu_left'), default=False)
    vertical_lines = models.BooleanField(_('vertical_lines'), default=False)
    top_navigation = models.BooleanField(_('top_navigation'), default=True)

    class Meta:
        verbose_name = _('Design Settings')
        verbose_name_plural = _('Design Settings')

    def __str__(self):
        return self.name


class FunctionalSettings(models.Model):
    name = models.CharField(_('name'), blank=True, null=True, max_length=200)

    project_category = models.BooleanField(_('project_category'), default=False)
    profile_category = models.BooleanField(_('profile_category'), default=False)

    contact_form = models.BooleanField(_('contact_form'), default=True)

    admin_exclude = models.CharField(default='name,admin_exclude', blank=True, null=True, max_length=600)

    class Meta:
        verbose_name = _('Functional Settings')
        verbose_name_plural = _('Functional Settings')

    def __str__(self):
        return self.name


class PageTexts(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('name'), blank=True, null=True, max_length=200, db_index=True),
        banner_big_text=RichTextUploadingField(_('banner big text'), blank=True, null=True),
        browser_title=models.CharField(_('browser_title'), blank=True, null=True, max_length=100),
        big_page_title=RichTextUploadingField(_('big page title'), blank=True, null=True),
        small_page_title=RichTextUploadingField(_('small page title'), blank=True, null=True),
        add_other_text=RichTextUploadingField(_('add_other_text'), blank=True, null=True),
    )
    add_name = models.BooleanField(_('add_name_to_bannertext'), default=False)
    active = models.BooleanField(_('active'), default=False)
    admin_exclude = models.CharField(default='name,admin_exclude', blank=True, null=True, max_length=600)

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

    preview_width = models.IntegerField(blank=True, null=True)
    preview_height = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _('Page Pictures')
        verbose_name_plural = _('Page Pictures')

    def __str__(self):
        return self.name
