from django.contrib import admin
from django import forms

# Register your models here.
from django.utils.safestring import mark_safe
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

    # def has_delete_permission(self, request, obj=None):
    #     # Disable delete
    #     return False

    def has_add_permission(self, request):
        # Disable add
        return False

    def get_fields(self, request, obj=None):
        fields = list(super(PageTextsAdmin, self).get_fields(request, obj))
        exclude_set = set()
        if obj:  # obj will be None on the add page, and something on change pages
            l = obj.admin_exclude.split(',')
            for a in l:
                exclude_set.add(a)
        return [f for f in fields if f not in exclude_set]


@admin.register(PagePictures)
class PagePicturesAdmin(TranslatableAdmin):
    save_on_top = True
    list_display = ('name', 'active')
    exclude = ('name', 'preview_height', 'preview_width', )

    readonly_fields = ['get_img_preview', ]

    def get_img_preview(self, obj):
        return mark_safe('<img src="{url}" width={w} height={h} />'.format(url=obj.image.url,
                                                                           w=obj.preview_width,
                                                                           h=obj.preview_height))

    class Meta:
        proxy = True

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    def has_add_permission(self, request):
        # Disable add
        return False




@admin.register(FunctionalSettings)
class FunctionalSettingsAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'project_category', 'profile_category', )

    class Meta:
        proxy = True

    def get_fields(self, request, obj=None):
        fields = list(super(FunctionalSettingsAdmin, self).get_fields(request, obj))
        exclude_set = set()
        if obj:  # obj will be None on the add page, and something on change pages
            l = obj.admin_exclude.split(',')
            for a in l:
                exclude_set.add(a)
        return [f for f in fields if f not in exclude_set]

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    def has_add_permission(self, request):
        # Disable add
        return False

