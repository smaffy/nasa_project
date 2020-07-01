from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _

from parler.models import TranslatableModel, TranslatedFields
from parler.utils.context import switch_language

BUTTON_COLOR_CHOICES = (
    ('default', 'default'),
    ('default-border', 'default-border'),
    ('primary', 'primary'),
    ('primary-border', 'primary-border'),
    ('success', 'success'),
    ('success-border', 'success-border'),
    ('info', 'info'),
    ('info-border', 'info-border'),
    ('warning', 'warning'),
    ('warning-border', 'warning-border'),
    ('danger', 'danger'),
    ('danger-border', 'danger-border'),
    ('link', 'link'),
    ('link-border', 'link-border'),
    ('disable', 'disable'),
)

BUTTON_FORM_CHOICES = (
    (' ', 'square default'),
    ('radius', 'radius'),
    ('circle', 'circle'),
    ('circle arrow', 'circle arrow'),
)

BUTTON_SIZE_CHOICES = (
    (' e-large', 'extralarge'),
    (' large', 'large'),
    (' ', 'default'),
    (' medium', 'medium'),
    (' small', 'small'),
)

HOME_V = (
    ('align-items-start', 'start'),
    ('align-items-center', 'center'),
    ('align-items-end', 'end'),
)

HOME = (
    ('ttl', 'left'),
    ('justify-content-center', 'center'),
    ('ttr', 'right'),
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
        home_big_banner_button=models.CharField(_('home_big_banner_button'), max_length=50, default='', null=True, blank=True),
        contact_button_text=models.CharField(_('contact_button_text'), max_length=50, default='', null=True, blank=True),
        callto_banner_button_text=models.CharField(_('callto_banner_button_text'), max_length=50, default='', null=True, blank=True),
    )
    active = models.BooleanField(_('active'), default=False)
    name = models.CharField(_('name'), default='design', blank=True, null=True, max_length=200, editable=False)
    info = models.CharField(_('info'), blank=True, null=True, max_length=200)

    button_color = models.CharField(_('button_color'), max_length=100, choices=BUTTON_COLOR_CHOICES, default='success', null=True, blank=True)
    button_size = models.CharField(_('button_size'), max_length=100, choices=BUTTON_SIZE_CHOICES, default=' ', null=True, blank=True)
    button_form = models.CharField(_('button_form'), max_length=100, choices=BUTTON_FORM_CHOICES, default='radius', null=True, blank=True)
    home_banner_text_align_vertical = models.CharField(_('home_banner_text_align_vertical'), max_length=100, choices=HOME_V, default='align-items-center', null=True, blank=True)
    home_banner_text_align_horizontal = models.CharField(_('home_banner_text_align_horizontal'), max_length=100, choices=HOME, default='justify-content-center', null=True, blank=True)
    font = models.CharField(_('fonts_for_all_site'), max_length=200, choices=FONT_CHOICES, default='Poppins, sans-serif', null=True, blank=True)
    social_icons_top_size = models.CharField(_('social_icons_top_size'), default=20, max_length=50, null=True, blank=True)
    social_icons_footer_size = models.CharField(_('social_icons_footer_size'), default=30, max_length=50, null=True, blank=True)

    # main_text_color = models.CharField(_('main_text_color (#000000 or black)'), max_length=200, null=True, blank=True)
    # main_menu_text_color = models.CharField(_('main_menu_text_color (#000000 or white)'), max_length=200, null=True, blank=True)
    # main_menu_text_size = models.CharField(_('main_menu_text_size'), default=14, max_length=50, null=True, blank=True)
    home_banner_height = models.CharField(_('home_banner_height px'), default=950, max_length=50, null=True, blank=True)
    banner_height = models.CharField(_('banner_height px'), default=300, max_length=50, null=True, blank=True)
    background_color = models.CharField(_('background_color (#000000 or black)'), max_length=200, null=True, blank=True)
    footer_background_color = models.CharField(_('footer_background_color (#000000 or black)'), max_length=200, null=True, blank=True)
    footer_font_color = models.CharField(_('footer_background_color (#000000 or black)'), max_length=200, null=True, blank=True)
    container_color = models.CharField(_('container_color (#000000 or black)'), max_length=200, null=True, blank=True)
    vertical_lines_color = models.CharField(_('vertical_lines_color (#000000 or black)'), max_length=200, null=True, blank=True)
    vertical_lines_width = models.CharField(_('vertical_lines_width px'), max_length=20, null=True, blank=True)

    overlay_default = models.BooleanField(_('overlay_default'), default=True)
    overlay = models.BooleanField(_('overlay'), default=True)
    overlay_opacity = models.CharField(_('overlay_opacity (from 0.1 to 0.9)'), max_length=50, null=True, blank=True)
    overlay_color = models.CharField(_('overlay_color (#000000 or black)'), max_length=200, null=True, blank=True)

    background_image = models.ImageField(_('background_image'), upload_to='images/background/', default=None, blank=True, null=True)
    logo_height = models.CharField(_('logo_height (30)'), default=30, max_length=50, null=True, blank=True)
    logo_width = models.CharField(_('logo_width (120)'), default=120, max_length=50, null=True, blank=True)
    background_image_on = models.BooleanField(_('background_image_on'), default=False)
    full_top_banner = models.BooleanField(_('full_top_banner'), default=True)
    menu_left = models.BooleanField(_('menu_left'), default=False)
    vertical_lines = models.BooleanField(_('vertical_lines'), default=False)
    top_navigation = models.BooleanField(_('top_navigation'), default=True)

    menu_text_color = models.CharField(_('menu_text_color (#000000 or white)'), max_length=200, null=True, blank=True)
    menu_text_size = models.CharField(_('menu_text_size px'), max_length=50, null=True, blank=True)
    menu_text_font = models.CharField(_('menu_text_font'), max_length=200, choices=FONT_CHOICES, null=True, blank=True)

    main_text_color = models.CharField(_('main_text_color (#000000 or black)'), max_length=200, null=True, blank=True)
    main_text_size = models.CharField(_('main_text_size px'), max_length=50, null=True, blank=True)
    main_text_font = models.CharField(_('main_text_font'), max_length=200, choices=FONT_CHOICES, null=True, blank=True)

    big_title_color = models.CharField(_('big_title_color (#000000 or black)'), max_length=200, null=True, blank=True)
    big_title_size = models.CharField(_('big_title_size px'), max_length=50, null=True, blank=True)
    big_title_font = models.CharField(_('big_title_font'), max_length=200, choices=FONT_CHOICES, null=True, blank=True)

    small_title_color = models.CharField(_('small_title_color (#000000 or white)'), max_length=200, null=True, blank=True)
    small_title_size = models.CharField(_('small_title_size px'), max_length=50, null=True, blank=True)
    small_title_font = models.CharField(_('small_title_font'), max_length=200, choices=FONT_CHOICES,null=True, blank=True)

    banner_title_color = models.CharField(_('banner_title_color (#000000 or white)'), max_length=200, null=True, blank=True)
    banner_title_size = models.CharField(_('banner_title_size px'), max_length=50, null=True, blank=True)
    banner_title_font = models.CharField(_('banner_title_font'), max_length=200, choices=FONT_CHOICES, null=True, blank=True)

    date_color = models.CharField(_('date_color (#000000 or white)'), max_length=200, null=True, blank=True)
    date_size = models.CharField(_('date_size px'), max_length=50, null=True, blank=True)
    date_font = models.CharField(_('date_font'), max_length=200, choices=FONT_CHOICES, default='default', null=True, blank=True)

    footer_text_color = models.CharField(_('footer_text_color (#000000 or white)'), max_length=200, null=True, blank=True)
    footer_text_size = models.CharField(_('footer_text_size px'), max_length=50, null=True, blank=True)
    footer_text_font = models.CharField(_('footer_text_font'), max_length=200, choices=FONT_CHOICES, default='default', null=True, blank=True)

    class Meta:
        verbose_name = _('Design Settings')
        verbose_name_plural = _('Design Settings')

    def __str__(self):
        return self.name

    def get_button_style(self):
        return self.button_size + ' ' + self.button_color + ' ' + self.button_form

    def get_style(self, size, color, font):
        t_size = t_color = t_font = ' '
        if size:
            t_size = 'font-size: {}px; '.format(size)
        if color:
            t_color = 'color: {}; '.format(color)
        if font:
            t_font = 'font-family: {}; '.format(font)
        return t_size + t_color + t_font

    def get_menu_text_style(self):
        return self.get_style(size=self.menu_text_size, color=self.menu_text_color, font=self.menu_text_font)

    def get_main_text_style(self):
        return self.get_style(self.main_text_size, self.main_text_color, self.main_text_font)

    def get_big_title_style(self):
        return self.get_style(self.big_title_size, self.big_title_color, self.big_title_font)

    def get_small_title_style(self):
        return self.get_style(self.small_title_size, self.small_title_color, self.small_title_font)

    def get_banner_title_style(self):
        return self.get_style(self.banner_title_size, self.banner_title_color, self.banner_title_font)

    def get_date_style(self):
        return self.get_style(self.date_size, self.date_color, self.date_font)

    def get_footer_text_style(self):
        return self.get_style(self.footer_text_size, self.footer_text_color, self.footer_text_font)


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
        banner_big_text=RichTextUploadingField(_('banner big text'), default='Banner Big Text', blank=True, null=True),
        browser_title=models.CharField(_('browser_title'), default='...', blank=True, null=True, max_length=100),
        big_page_title=RichTextUploadingField(_('big page title'), default='Big page title', blank=True, null=True),
        small_page_title=RichTextUploadingField(_('small page title'), default='Small page title', blank=True, null=True),
        add_other_text=RichTextUploadingField(_('add_other_text'), default='other text', blank=True, null=True),
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
