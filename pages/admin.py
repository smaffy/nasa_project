from django.contrib import admin
from django.template.defaultfilters import truncatewords

from .models import Project, Profile, News, Service, ProjectImage
from .forms import ProjectAdminForm, ProfileAdminForm, NewsAdminForm


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


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    form = ProfileAdminForm
    list_display = (
        'first_name', 'last_name', 'slug', 'phone_number', 'email',
        'short_description',
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = (
        'title', 'slug',
        'short_description',
    )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    form = NewsAdminForm
    list_display = (
        'title',
        'short_description',
    )


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = (
        'image',
        'index',
    )

