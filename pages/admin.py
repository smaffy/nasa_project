from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db import models
from django.template.defaultfilters import truncatewords

from .models import Project, Profile, News, Service, ProjectImage, ProjectCategory, ProfileCategory
from .forms import ProjectAdminForm, ProfileAdminForm, NewsAdminForm
from parler.admin import TranslatableAdmin, TranslatableStackedInline

#
# class TranslatableSite(TranslatableModel, Site):
#     class Meta:
#         proxy = True
#
#     translations = TranslatedFields()
#
#
# class NewSiteAdmin(TranslatableAdmin, SiteAdmin):
#     pass
#
#
# admin.site.unregister(Site)
# admin.site.register(TranslatableSite, NewSiteAdmin)


class ImageInline(admin.StackedInline):
    model = ProjectImage
    max_num = 10
    extra = 0


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
            "fields": ('first_image', )
        }),
        (None, {
            "fields": ('short_description', 'description',)
        }),
    )
    # prepopulated_fields = {'slug': ('title',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}

    class Meta:
        proxy = True


@admin.register(Profile)
class ProfileAdmin(TranslatableAdmin):
    save_on_top = True
    save_as = True
    form = ProfileAdminForm
    inlines = [ProjectsInline, ]
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
            "fields": ('image',)
        }),
        (None, {
            "fields": ('short_description', 'description',)
        }),
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('first_name', 'last_name',)}

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

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}

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
    # prepopulated_fields = {'slug': ('title',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}

    class Meta:
        proxy = True


@admin.register(ProjectImage)
class ProjectImageAdmin(ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = (
        'image',
        'index',
    )


