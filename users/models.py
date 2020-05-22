from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    address = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to='images/users/', default='images/defaults/logo.png')

    email = models.EmailField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    time_for_colling = models.CharField(max_length=50, null=True, blank=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'user'
        default_related_name = 'user'

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
