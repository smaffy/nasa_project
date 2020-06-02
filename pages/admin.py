from django.contrib import admin
from django.contrib.sites.admin import SiteAdmin
from django.template.defaultfilters import truncatewords
from parler.admin import TranslatableAdmin

from .models import Project, Profile, News, Service, ProjectImage, ProjectCategory, ProfileCategory
from .forms import ProjectAdminForm, ProfileAdminForm, NewsAdminForm
from django.contrib.sites.models import Site
from parler.models import TranslatableModel, TranslatedFields
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site
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


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    form = ProjectAdminForm
    list_display = (
        'title',
        'client', 'website', 'completed',
        'short_description',
    )
    inlines = [ImageInline, ]
    # prepopulated_fields = {'slug': ('title',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    form = ProfileAdminForm
    list_display = (
        'first_name', 'last_name', 'slug',
        'short_description',
    )
    # prepopulated_fields = {'slug': ('first_name', 'last_name',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('first_name', 'last_name',)}


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


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = (
        'title', 'category_slug',
    )
    # prepopulated_fields = {'category_slug': ('title',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {'category_slug': ('title',)}


@admin.register(ProfileCategory)
class ProfileCategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = (
        'title', 'category_slug',
    )
    # prepopulated_fields = {'category_slug': ('title',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {'category_slug': ('title',)}


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
class ProjectImageAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = (
        'image',
        'index',
    )

