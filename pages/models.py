import datetime
from datetime import date

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import truncatewords


def group(iterable, mycount):
    it = len(list(iterable))
    a = list(zip(*[iter(iterable)] * mycount))
    b = len(a) * mycount
    c = it - b
    if c > 0:
        a.append(list(list(iterable)[-c:]))
    return a


class Service(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    short_description = models.TextField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Services'

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


class ProfileCategory(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category_slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'

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


class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    profile_category = models.ManyToManyField(ProfileCategory, default=None, related_name='profile_category')
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    start_work = models.DateField(auto_now=False, auto_now_add=False)
    short_description = models.TextField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/profile/', default='images/defaults/project-details.jpg')

    class Meta:
        ordering = ['start_work']
        verbose_name_plural = 'Profiles'

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


class News(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    short_description = models.TextField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/news/', default='images/defaults/news.jpg')
    published = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-published']

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


class ProjectCategory(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category_slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'

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


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    project_category = models.ManyToManyField(ProjectCategory, default=None, related_name='project_category')
    project_team = models.ManyToManyField(Profile, default=None, related_name='team')
    client = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    completed = models.DateField(auto_now=False, auto_now_add=False)
    short_description = models.TextField()
    description = models.TextField(blank=True, null=True)
    first_image = models.ImageField(upload_to='images/projects/', default='images/defaults/project-details.jpg')
    ind = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['-completed']
        verbose_name_plural = 'Projects'

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
    image = models.ImageField(upload_to='images/projects/', verbose_name='product_image', default='images/products/project_detail.jpg')
    index = models.PositiveIntegerField(blank=True, null=True, default=0)

    class Meta:
        ordering = ['index']
        verbose_name_plural = 'ProjectImages'

