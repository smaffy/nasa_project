from django.db import models
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import truncatewords


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    client = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    completed = models.DateField(auto_now=False, auto_now_add=False)
    short_description = models.TextField()
    description = models.TextField(blank=True, null=True)
    first_image = models.ImageField(upload_to='images/projects/', default='images/defaults/project-details.jpg')

    class Meta:
        ordering = ['completed']
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            if len(self.title) < 15:
                self.slug = self.title
            else:
                self.slug = truncatewords(self.title, 3)
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:projects_detail', kwargs={'slug': self.slug, })


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
                self.slug = self.title
            else:
                self.slug = truncatewords(self.title, 3)
        super(Service, self).save(*args, **kwargs)


class Profile(models.Model):
    first_name = models.CharField(max_length=200, unique=True)
    last_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
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
            self.slug = self.first_name + '_' + self.last_name
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:profile', kwargs={'slug': self.slug, })


class News(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    short_description = models.TextField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/news/', default='images/defaults/news.jpg')

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if len(self.title) < 15:
            self.slug = self.title
        else:
            self.slug = truncatewords(self.title, 3)
        super(News, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:news_detail', kwargs={'slug': self.slug, })


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='images/projects/', verbose_name='product_image', default='images/products/project_detail.jpg')
    index = models.PositiveIntegerField(blank=True, null=True, default=0)

    class Meta:
        ordering = ['index']
        verbose_name_plural = 'ProjectImages'
