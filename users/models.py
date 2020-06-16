from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
# _(''),


class CustomUser(AbstractUser):
    first_name = models.CharField(_('first_name'), max_length=50, null=True, blank=True)
    last_name = models.CharField(_('last_name'), max_length=50, null=True, blank=True)
    slug = models.SlugField(_('slug'), max_length=50, null=True, blank=True)

    address = models.CharField(_('address'), max_length=250, null=True, blank=True)
    postal_code = models.CharField(_('postal_code'), max_length=20, null=True, blank=True)
    city = models.CharField(_('city'), max_length=100, null=True, blank=True)
    country = models.CharField(_('country'), max_length=100, null=True, blank=True)
    company_name = models.CharField(_('company_name'), max_length=100, null=True, blank=True)
    logo = models.ImageField(_('logo_120x30'), upload_to='images/users/', default='images/defaults/logo.png')

    registation_number = models.CharField(_('registation_number'), max_length=50, blank=True, null=True)
    address_inline = models.CharField(_('address_inline'), max_length=300, blank=True, null=True)
    info = models.TextField(_('info'), blank=True, null=True)

    email = models.EmailField(_('email'), blank=True, null=True)
    phone_number = PhoneNumberField(_('phone_number'), blank=True, null=True)
    time_for_colling = models.CharField(_('time_for_colling'), max_length=50, null=True, blank=True)
    facebook = models.URLField(_('facebook'), max_length=200, blank=True, null=True)
    instagram = models.URLField(_('instagram'), max_length=200, blank=True, null=True)
    twitter = models.URLField(_('twitter'), max_length=200, blank=True, null=True)
    active = models.BooleanField(_('active'), default=False)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('user')
        default_related_name = _('user')

    def get_name(self):
        if self.company_name:
            return self.company_name
        elif self.first_name and self.last_name:
            name = '%s %s' % (self.first_name, self.last_name)
            return name
        else:
            return self.username

    def __str__(self):
        if self.company_name:
            return self.company_name
        elif self.first_name and self.last_name:
            name = '%s_%s' % (self.first_name, self.last_name)
            return name
        else:
            return self.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.get_name())
        super(CustomUser, self).save(*args, **kwargs)
