import datetime
from datetime import date

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import truncatewords

from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields, TranslatedFieldsModelMixin
# _(''),


def group(iterable, mycount):
    it = len(list(iterable))
    a = list(zip(*[iter(iterable)] * mycount))
    b = len(a) * mycount
    c = it - b
    if c > 0:
        a.append(list(list(iterable)[-c:]))
    return a


class Service(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=200, unique=True, db_index=True),
        slug = models.SlugField(_('slug'), max_length=200, unique=True, blank=True, null=True, db_index=True),
        short_description = models.TextField(_('short_description')),
        description = models.TextField(_('description'), blank=True, null=True),

    )

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            if len(self.title) < 15:
                self.slug = slugify(self.title)
            else:
                self.slug = slugify(truncatewords(self.title, 3))
        super(Service, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:service_detail', kwargs={'slug': self.slug, })


class ProfileCategory(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=200, unique=True, db_index=True),
        category_slug = models.SlugField(_('category_slug'), db_index=True, max_length=200, unique=True, blank=True, null=True),
    )

    class Meta:
        # ordering = ['title']
        verbose_name = _('Profile Category')
        verbose_name_plural = _('Profile Categories')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.category_slug:
            if len(self.title) < 15:
                self.category_slug = slugify(self.title)
            else:
                self.category_slug = slugify(truncatewords(self.title, 3))
        super(ProfileCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:profile_category', kwargs={'category_slug': self.category_slug, })


class Profile(TranslatableModel):
    translations = TranslatedFields(
        first_name = models.CharField(_('first name'), max_length=200),
        last_name = models.CharField(_('last name'), max_length=200),
        slug = models.SlugField(_('slug'), max_length=200, unique=True, blank=True, null=True, db_index=True),
        short_description = models.TextField(_('short_description')),
        description = models.TextField(_('description'), blank=True, null=True),
    )

    profile_category = models.ManyToManyField(ProfileCategory, blank=True, default=None, related_name='profile_category')
    facebook = models.URLField(_('facebook'), max_length=200, blank=True, null=True)
    twitter = models.URLField(_('twitter'), max_length=200, blank=True, null=True)
    phone_number = PhoneNumberField(_('phone number'), blank=True, null=True)
    email = models.EmailField(_('email'), blank=True, null=True)
    start_work = models.DateField(_('start_work'), default=timezone.now)

    image = models.ImageField(_('profile image'), upload_to='images/profile/', default='images/defaults/project-details.jpg')

    class Meta:
        # ordering = ['start_work']
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def get_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return self.get_name()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.get_name())
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:profile', kwargs={'slug': self.slug, })

    def get_short_description(self):
        desc = truncatewords(self.short_description, 25) + '...'
        return desc


class News(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=200, unique=True, db_index=True),
        slug = models.SlugField(_('slug'), max_length=200, unique=True, blank=True, null=True, db_index=True),
        short_description = models.TextField(_('short_description'), ),
        description = models.TextField(_('description'), blank=True, null=True),
    )
    image = models.ImageField(_('news image'), upload_to='images/news/', default='images/defaults/news.jpg')
    published = models.DateField(_('published'), default=datetime.date.today)

    class Meta:
        # ordering = ['-published']
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if len(self.title) < 15:
            self.slug = slugify(self.title)
        else:
            self.slug = slugify(truncatewords(self.title, 3))
        super(News, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:news_detail', kwargs={'slug': self.slug, })


class ProjectCategory(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=200, unique=True, db_index=True),
        category_slug = models.SlugField(_('category_slug'), db_index=True, max_length=200, unique=True, blank=True, null=True)
    )

    class Meta:
        # ordering = ['title']
        verbose_name = _('Project Category')
        verbose_name_plural = _('Project Categories')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.category_slug:
            if len(self.title) < 15:
                self.category_slug = slugify(self.title)
            else:
                self.category_slug = slugify(truncatewords(self.title, 3))
        super(ProjectCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:projects_category', kwargs={'category_slug': self.category_slug, })


class Project(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'), db_index=True, max_length=200, unique=True),
        slug = models.SlugField(_('slug'), db_index=True, max_length=200, unique=True, blank=True, null=True),
        short_description = models.TextField(_('short_description'), ),
        description = models.TextField(_('description'), blank=True, null=True),
    )

    project_category = models.ManyToManyField(ProjectCategory, blank=True, default=None, related_name='project_category')
    project_team = models.ManyToManyField(Profile, blank=True, default=None, related_name='projects')
    client = models.CharField(_('client'), max_length=200, blank=True, null=True)
    website = models.URLField(_('website'), max_length=200, blank=True, null=True)
    completed = models.DateField(_('completed'), default=timezone.now)
    first_image = models.ImageField(_('first_image'), upload_to='images/projects/', default='images/defaults/project-details.jpg')
    index = models.PositiveSmallIntegerField(blank=True, null=True, default=0)

    class Meta:
        # ordering = ['-completed']
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            if len(self.title) < 15:
                self.slug = slugify(self.title)
            else:
                self.slug = slugify(truncatewords(self.title, 3))
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:projects_detail', kwargs={'slug': self.slug, })

    def get_images(self):
        images = ProjectImage.objects.filter(project__slug=self.slug)
        return group(images, 4)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(_('project image'), upload_to='images/projects/', default='images/products/project_detail.jpg')
    index = models.PositiveSmallIntegerField(blank=True, null=True, default=0)

    class Meta:
        ordering = ['index']
        verbose_name = _('Project Image')
        verbose_name_plural = _('Project Images')
