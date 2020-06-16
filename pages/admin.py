from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db import models
from django.template.defaultfilters import truncatewords
from django.utils.safestring import mark_safe

from .models import Project, Profile, News, Service, ProjectImage, ProjectCategory, ProfileCategory
from .forms import ProjectAdminForm, ProfileAdminForm, NewsAdminForm
from parler.admin import TranslatableAdmin, TranslatableStackedInline


class ImageInline(admin.StackedInline):
    model = ProjectImage
    max_num = 10
    extra = 0

    readonly_fields = ['get_img_preview', ]

    def get_img_preview(self, obj):
        return mark_safe('<img src="{url}" width=200 height=150 />'.format(url=obj.image.url))


class ProjectsInline(admin.StackedInline):
    model = Profile.projects.through
    max_num = 10
    extra = 0


@admin.register(Project)
class ProjectAdmin(TranslatableAdmin):
    save_on_top = True
    save_as = True
    form = ProjectAdminForm
    list_display = (
        'title',
        'client', 'website', 'completed',
        'short_description',
    )
    inlines = [ImageInline, ]
    readonly_fields = ['get_img_preview', ]

    fieldsets = (
        ('Title', {
            "fields": ('title', 'slug', )
        }),
        (None, {
            "fields": ('project_category', 'project_team', )
        }),
        (None, {
            "fields": ('client', 'website', 'completed', 'index',)
        }),
        (None, {
            "fields": ('first_image', 'get_img_preview',)
        }),
        (None, {
            "fields": ('short_description', 'description',)
        }),
    )
    # prepopulated_fields = {'slug': ('title',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}

    def get_img_preview(self, obj):
        return mark_safe('<img src="{url}" width=300 height=200 />'.format(url=obj.first_image.url))

    class Meta:
        proxy = True


@admin.register(Profile)
class ProfileAdmin(TranslatableAdmin):
    save_on_top = True
    save_as = True
    form = ProfileAdminForm
    inlines = [ProjectsInline, ]
    readonly_fields = ['get_img_preview', ]
    list_display = (
        'first_name', 'last_name', 'slug',
        'short_description',
    )
    # prepopulated_fields = {'slug': ('first_name', 'last_name',)}
    fieldsets = (
        ('Title', {
            "fields": ('first_name', 'last_name', 'slug', )
        }),
        (None, {
            "fields": ('profile_category',)
        }),
        ('Social', {
            "fields": ('facebook', 'twitter',)
        }),
        ('Contact', {
            "fields": ('phone_number', 'email',)
        }),
        (None, {
            "fields": ('start_work',)
        }),
        (None, {
            "fields": ('image', 'get_img_preview',)
        }),
        (None, {
            "fields": ('short_description', 'description')
        }),
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('first_name', 'last_name',)}

    def get_img_preview(self, obj):
        return mark_safe('<img src="{url}" width=300 height=300 />'.format(url=obj.image.url))

    class Meta:
        proxy = True


@admin.register(Service)
class ServiceAdmin(TranslatableAdmin):
    save_on_top = True
    save_as = True
    list_display = (
        'title', 'slug',
         'short_description',
    )
    readonly_fields = ['get_img_preview', ]

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}

    def get_img_preview(self, obj):
        return mark_safe('<img src="{url}" width=300 height=200 />'.format(url=obj.image.url))

    class Meta:
        proxy = True


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(TranslatableAdmin):
    save_on_top = True
    save_as = True

    list_display = (
        'title', 'category_slug',
    )
    # prepopulated_fields = {'category_slug': ('title',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {'category_slug': ('title',)}

    class Meta:
        proxy = True


@admin.register(ProfileCategory)
class ProfileCategoryAdmin(TranslatableAdmin):
    save_on_top = True
    save_as = True
    list_display = (
        'title', 'category_slug',
    )
    # prepopulated_fields = {'category_slug': ('title',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {'category_slug': ('title',)}

    class Meta:
        proxy = True


@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    save_on_top = True
    save_as = True
    form = NewsAdminForm
    list_display = (
        'title',
        'short_description',
    )
    readonly_fields = ['get_img_preview', ]

    # prepopulated_fields = {'slug': ('title',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}

    def get_img_preview(self, obj):
        return mark_safe('<img src="{url}" width=300 height=200 />'.format(url=obj.image.url))

    class Meta:
        proxy = True


@admin.register(ProjectImage)
class ProjectImageAdmin(ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = (
        'image',
        'project',
        'index',
        'get_img_preview',
    )
    readonly_fields = ['get_img_preview', ]

    def get_img_preview(self, obj):
        return mark_safe('<img src="{url}" width=200 height=150 />'.format(url=obj.image.url))



