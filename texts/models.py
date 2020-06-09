from django.db import models
from django.utils.translation import gettext_lazy as _

from parler.models import TranslatableModel, TranslatedFields
from parler.utils.context import switch_language


class PageTexts(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('name'), blank=True, null=True, max_length=200, db_index=True),
        big_page_title=models.TextField(_('big page title'), blank=True, null=True),
        small_page_title=models.TextField(_('small page title'), blank=True, null=True),
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
