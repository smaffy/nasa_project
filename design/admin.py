from django.contrib import admin
from django import forms

# Register your models here.
from django.utils.safestring import mark_safe
from parler.admin import TranslatableAdmin

from .forms import PageTextsAdminForm
from .models import PageTexts, PagePictures, FunctionalSettings, DesignSettings


def delete_design(TranslatableAdmin, request, queryset):
    DesignSettings.objects.exclude(info='default').delete()


def create_or_clear_default_design(TranslatableAdmin, request, queryset):
    DesignSettings.objects.filter(info='default').delete()
    DesignSettings.objects.create(info='default')


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
    list_display = ('name',)

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


@admin.register(DesignSettings)
class DesignSettingsAdmin(TranslatableAdmin):
    save_on_top = True
    actions = [delete_design, create_or_clear_default_design]
    list_display = ('name', 'info')
    exclude = ('name',)
    readonly_fields = ['get_img_preview', 'get_font_preview']

    fieldsets = (
        (None, {
            "fields": ('active', 'info',)
        }),
        ('ON/OFF', {
            "fields": ('background_image_on', 'full_top_banner', 'menu_left', 'vertical_lines', 'top_navigation',)
        }),
        ('Main', {
            "fields": ('font', 'get_font_preview', 'main_text_color', 'background_color', 'container_color', 'background_image', 'get_img_preview',)
        }),
        ('Home Banner', {
            "fields": ('home_banner_text_align_vertical', 'home_banner_text_align_horizontal', 'home_banner_height',)
        }),
        ('Icons', {
            "fields": ('social_icons_top_size', 'social_icons_footer_size',)
        }),
        ('Main Menu', {
            "fields": ('main_menu_text_color', 'main_menu_text_size', 'banner_height', )
        }),
        ('Vertical Lines', {
            "fields": ('vertical_lines_color', 'vertical_lines_width',)
        }),
        ('Overlay Header Menu', {
            "fields": ('overlay_default', 'overlay', 'overlay_opacity', 'overlay_color',)
        }),
        ('Buttons', {
            "fields": ('button_color', 'button_size', 'button_form', 'home_big_banner_button')
        }),
        ('Logo', {
            "fields": ('logo_height', 'logo_width',)
        }),
        ('Footer', {
            "fields": ('footer_background_color',)
        }),
        # (None, {
        #     "fields": ('active', 'info',)
        # }),
        # (None, {
        #     "fields": ('active', 'info',)
        # }),
    )

    class Meta:
        proxy = True

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    # def has_add_permission(self, request):
    #     # Disable add
    #     return False

    def get_img_preview(self, obj):
        if obj.background_image.url:
            return mark_safe('<img src="{url}" height=400 />'.format(url=obj.background_image.url))
        else:
            return 'no image'

    def get_font_preview(self, obj):
        if obj.font == "Poppins, sans-serif":
            a = '<link href="https://fonts.googleapis.com/css?family=Poppins:100,200,400,300,500,600,700" rel="stylesheet">'
        if obj.font == "Sriracha, cursive":
            a = '<link href="https://fonts.googleapis.com/css2?family=Sriracha&display=swap" rel="stylesheet">'
        if obj.font == "Lato, sans-serif":
            a = '<link href="https://fonts.googleapis.com/css2?family=Lato&display=swap" rel="stylesheet">'
        if obj.font == "Roboto, sans-serif":
            a = '<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">'
        if obj.font == "Open Sans, sans-serif":
            a = '<link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">'
        if obj.font == "Caveat, cursive":
            a = '<link href="https://fonts.googleapis.com/css2?family=Caveat&display=swap" rel="stylesheet">'
        if obj.font == "Yanone Kaffeesatz, sans-serif":
            a = '<link href="https://fonts.googleapis.com/css2?family=Yanone+Kaffeesatz&display=swap" rel="stylesheet">'
        if obj.font == "Inconsolata, monospace":
            a = '<link href="https://fonts.googleapis.com/css2?family=Inconsolata&display=swap" rel="stylesheet">'
        if obj.font == "Rubik, sans-serif":
            a = '<link href="https://fonts.googleapis.com/css2?family=Rubik&display=swap" rel="stylesheet">'
        if obj.font == "Merriweather, serif":
            a = '<link href="https://fonts.googleapis.com/css2?family=Merriweather&display=swap" rel="stylesheet">'
        if obj.font == "Arizonia, cursive":
            a = '<link href="https://fonts.googleapis.com/css2?family=Arizonia&display=swap" rel="stylesheet">'
        if obj.font == "Permanent Marker, cursive":
            a = '<link href="https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap" rel="stylesheet">'
        if obj.font == "Marck Script, cursive":
            a = '<link href="https://fonts.googleapis.com/css2?family=Marck+Script&display=swap" rel="stylesheet">'
        else:
            a = '<link href="https://fonts.googleapis.com/css?family=Poppins:100,200,400,300,500,600,700" rel="stylesheet">'

        ttext = a + """
    
            {f}:     <p style="font-family: {f}; color:green">Almost before we knew it, we had left the ground.</p>
        """
        return mark_safe(ttext.format(f=obj.font))


