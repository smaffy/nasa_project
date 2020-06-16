from django.contrib import admin
from django import forms

# Register your models here.
from parler.admin import TranslatableAdmin

from .forms import PageTextsAdminForm
from .models import PageTexts, PagePictures, FunctionalSettings


@admin.register(PageTexts)
class PageTextsAdmin(TranslatableAdmin):
    save_on_top = True
    list_display = ('name', 'active')
    form = PageTextsAdminForm

    class Meta:
        proxy = True
    #
    # def has_delete_permission(self, request, obj=None):
    #     # Disable delete
    #     return False
    #
    # def has_add_permission(self, request):
    #     # Disable add
    #     return False


@admin.register(PagePictures)
class PagePicturesAdmin(TranslatableAdmin):
    save_on_top = True
    list_display = ('name', 'active')
    exclude = ('name', )

    class Meta:
        proxy = True

    # def has_delete_permission(self, request, obj=None):
    #     # Disable delete
    #     return False
    #
    # def has_add_permission(self, request):
    #     # Disable add
    #     return False
    #
    #


@admin.register(FunctionalSettings)
class FunctionalSettingsAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'project_category', 'profile_category', )
    exclude = ('name', )

    class Meta:
        proxy = True

    # def has_delete_permission(self, request, obj=None):
    #     # Disable delete
    #     return False
    #
    # def has_add_permission(self, request):
    #     # Disable add
    #     return False
    #
    #