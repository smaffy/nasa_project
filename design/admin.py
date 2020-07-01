from django.contrib import admin
from django import forms

# Register your models here.
from django.utils.safestring import mark_safe
from parler.admin import TranslatableAdmin

from users.models import CustomUser
from .forms import PageTextsAdminForm
from .models import PageTexts, PagePictures, FunctionalSettings, DesignSettings

mystyle = """
    <style>
        .genric-btn {
          display: inline-block;
          outline: none;
          line-height: 40px;
          padding: 0 30px;
          font-size: .8em;
          text-align: center;
          text-decoration: none;
          font-weight: 500;
          cursor: pointer;
          -webkit-transition: all 0.3s ease 0s;
          -moz-transition: all 0.3s ease 0s;
          -o-transition: all 0.3s ease 0s;
          transition: all 0.3s ease 0s;
        }
    
        .genric-btn:focus {
          outline: none;
        }
    
        .genric-btn.e-large {
          padding: 0 40px;
          line-height: 50px;
        }
    
        .genric-btn.large {
          line-height: 45px;
        }
    
        .genric-btn.medium {
          line-height: 30px;
        }
    
        .genric-btn.small {
          line-height: 25px;
        }
    
        .genric-btn.radius {
          border-radius: 3px;
        }
    
        .genric-btn.circle {
          border-radius: 20px;
        }
    
        .genric-btn.arrow {
          display: -webkit-inline-box;
          display: -ms-inline-flexbox;
          display: inline-flex;
          -webkit-box-align: center;
          -ms-flex-align: center;
          align-items: center;
        }
    
        .genric-btn.arrow span {
          margin-left: 10px;
        }
    
        .genric-btn.default {
          color: #222;
          background: #f9f9ff;
          border: 1px solid transparent;
        }
    
        .genric-btn.default:hover {
          border: 1px solid #f9f9ff;
          background:transparent;
        }
    
        .genric-btn.default-border {
          border: 1px solid #f9f9ff;
          background: transparent;
        }
    
        .genric-btn.default-border:hover {
          color: #222;
          background: #f9f9ff;
          border: 1px solid transparent;
        }
    
        .genric-btn.primary {
          color: #fff;
          background: #c6b069;
          border: 1px solid transparent;
        }
    
        .genric-btn.primary:hover {
          color: #c6b069;
          border: 1px solid #c6b069;
          background: transparent;
        }
    
        .genric-btn.primary-border {
          color: #c6b069;
          border: 1px solid #c6b069;
          background: transparent;
        }
    
        .genric-btn.primary-border:hover {
          color: #fff;
          background: #c6b069;
          border: 1px solid transparent;
        }
    
        .genric-btn.success {
          color: transparent;
          background: #4cd3e3;
          border: 1px solid transparent;
        }
    
        .genric-btn.success:hover {
          color: #4cd3e3;
          border: 1px solid #4cd3e3;
          background: transparent;
        }
    
        .genric-btn.success-border {
          color: #4cd3e3;
          border: 1px solid #4cd3e3;
          background: transparent;
        }
    
        .genric-btn.success-border:hover {
          color: #fff;
          background: #4cd3e3;
          border: 1px solid transparent;
        }
    
        .genric-btn.info {
          color: #fff;
          background: #38a4ff;
          border: 1px solid transparent;
        }
    
        .genric-btn.info:hover {
          color: #38a4ff;
          border: 1px solid #38a4ff;
          background: transparent;
        }
    
        .genric-btn.info-border {
          color: #38a4ff;
          border: 1px solid #38a4ff;
          background: transparent;
        }
    
        .genric-btn.info-border:hover {
          color: #fff;
          background: #38a4ff;
          border: 1px solid transparent;
        }
    
        .genric-btn.warning {
          color: #fff;
          background: #f4e700;
          border: 1px solid transparent;
        }
    
        .genric-btn.warning:hover {
          color: #f4e700;
          border: 1px solid #f4e700;
          background: transparent;
        }
    
        .genric-btn.warning-border {
          color: #f4e700;
          border: 1px solid #f4e700;
          background: transparent;
        }
    
        .genric-btn.warning-border:hover {
          color: #fff;
          background: #f4e700;
          border: 1px solid transparent;
        }
    
        .genric-btn.danger {
          color: #fff;
          background: #f44a40;
          border: 1px solid transparent;
        }
    
        .genric-btn.danger:hover {
          color: #f44a40;
          border: 1px solid #f44a40;
          background: transparent;
        }
    
        .genric-btn.danger-border {
          color: #f44a40;
          border: 1px solid #f44a40;
          background: transparent;
        }
    
        .genric-btn.danger-border:hover {
          color: transparent;
          background: #f44a40;
          border: 1px solid transparent;
        }
    
        .genric-btn.link {
          color: #222;
          background: #f9f9ff;
          text-decoration: underline;
          border: 1px solid transparent;
        }
    
        .genric-btn.link:hover {
          color: #222;
          border: 1px solid #f9f9ff;
          background: transparent;
        }
    
        .genric-btn.link-border {
          color: #222;
          border: 1px solid #f9f9ff;
          background: transparent;
          text-decoration: underline;
        }
    
        .genric-btn.link-border:hover {
          color: #222;
          background: #f9f9ff;
          border: 1px solid transparent;
        }
    
        .genric-btn.disable {
          color: #222,0.3;
          background: #f9f9ff;
          border: 1px solid transparent;
          cursor: not-allowed;
        }
    </style>
        """

mytext = '<p style="background-color: #e8e8e8; padding: 5px;{}">We knew it.</p>'


def activate(TranslatableAdmin, request, queryset):
    queryset.update(active=True)


def deactivate(TranslatableAdmin, request, queryset):
    queryset.update(active=False)


def delete_design(TranslatableAdmin, request, queryset):
    DesignSettings.objects.exclude(info='default').delete()


def create_or_clear_default_design(TranslatableAdmin, request, queryset):
    DesignSettings.objects.filter(info='default').delete()
    DesignSettings.objects.create(info='default')


@admin.register(PageTexts)
class PageTextsAdmin(TranslatableAdmin):
    save_on_top = True
    list_display = ('name', 'active')
    actions = [activate, deactivate]

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

    readonly_fields = ['get_img_preview', 'get_img_preview_with_overlay']

    def get_img_preview(self, obj):
        return mark_safe('<img src="{url}" width={w} height={h} />'.format(url=obj.image.url,
                                                                           w=obj.preview_width,
                                                                           h=obj.preview_height))

    def get_img_preview_with_overlay(self, obj):
        # return mark_safe('<img src="{url}" width={w} height={h} />'.format(url=obj.image.url,
        #                                                                    w=obj.preview_width,
        #                                                                    h=obj.preview_height))
        design = DesignSettings.objects.language('en').filter(name='design', active=True).first()

        if design.main_menu_text_color:
            main_menu_text_color = design.main_menu_text_color
        else:
            main_menu_text_color = 'white'

        if design.overlay_color and design.overlay_opacity and obj.image:
            fpic = mark_safe('<div style="text-align: center; background: url({im}) center; height: {h}px; width: {w}px;"><div class="overlay overlay-bg" style="background-color: {b}; color: {t}; opacity: {o}; height: {h}px; width: {w}px; border: 1px solid gray; color: {t}"> <b>Menu Text</b> </div></div>'.format(
                    im=obj.image.url, b=design.overlay_color, t=main_menu_text_color, o=design.overlay_opacity, w=obj.preview_width, h=obj.preview_height))
        else:
            fpic = mark_safe('<div style="text-align: center; background: url({im}) center; height: {h}px; width: {w}px; color={t}"><div class="overlay overlay-bg"> <b>Menu Text</b> </div></div>'.format(im=obj.image.url, b=design.overlay_color, t=main_menu_text_color, o=design.overlay_opacity, w=obj.preview_width, h=obj.preview_height))
        return fpic

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
    readonly_fields = [
        'get_img_preview',
        'get_font_preview',
        'preview_background_color',
        'preview_container_color',
        'preview_vertical_lines_color',
        'preview_main_menu_text_color',
        'preview_overlay',
        'preview_footer',
        'get_logo_preview',
        'get_home_button_preview',
        'preview_menu_text_style',
        'preview_main_text_style',
        'preview_big_title_style',
        'preview_small_title_style',
        'preview_banner_title_style',
        'preview_date_style',
        'preview_footer_text_style'
    ]

    fieldsets = (
        (None, {
            "fields": ('active', 'info',)
        }),
        ('ON/OFF', {
            "fields": ('background_image_on', 'full_top_banner', 'menu_left', 'vertical_lines', 'top_navigation',)
        }),
        ('Main', {
            "fields": ('get_font_preview', ('background_color', 'preview_background_color',), ('container_color', 'preview_container_color',), 'background_image', 'get_img_preview',)
        }),
        ('Text styles', {
            "fields": (
                'font',
                ('main_text_color', 'main_text_size', 'main_text_font', 'preview_main_text_style',),
                ('menu_text_color', 'menu_text_size', 'menu_text_font', 'preview_menu_text_style',),
                ('big_title_color', 'big_title_size', 'big_title_font', 'preview_big_title_style',),
                ('small_title_color', 'small_title_size', 'small_title_font', 'preview_small_title_style',),
                ('banner_title_color', 'banner_title_size', 'banner_title_font', 'preview_banner_title_style',),
                ('date_color', 'date_size', 'date_font', 'preview_date_style',),
                ('footer_text_color', 'footer_text_size', 'footer_text_font', 'preview_footer_text_style',),
            )
        }),

        ('Home Banner', {
            "fields": ('home_banner_text_align_vertical', 'home_banner_text_align_horizontal', 'home_banner_height', 'banner_height',)
        }),
        ('Icons', {
            "fields": ('social_icons_top_size', 'social_icons_footer_size',)
        }),
        ('Vertical Lines', {
            "fields": (('vertical_lines_color', 'preview_vertical_lines_color',), 'vertical_lines_width',)
        }),
        ('Overlay Header Menu', {
            "fields": ('overlay_default', 'overlay', 'overlay_opacity', 'overlay_color', 'preview_overlay')
        }),
        ('Buttons', {
            "fields": ('button_color', 'button_size', 'button_form', 'home_big_banner_button', 'contact_button_text', 'callto_banner_button_text', 'get_home_button_preview')
        }),
        ('Logo', {
            "fields": ('logo_height', 'logo_width', 'get_logo_preview')
        }),
        ('Footer', {
            "fields": ('footer_font_color', 'footer_background_color', 'preview_footer')
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

    def preview_background_color(self, obj):
        if obj.background_color:
            return mark_safe('<div style="background-color: {}; height: 25px; width: 100px; border: 1px solid gray;"> </div>'.format(obj.background_color))

    # def preview_main_text_color(self, obj):
    #     if obj.container_color and obj.main_text_color:
    #         return mark_safe('<div style="background-color: {b}; color={t}; height: 25px; width: 100px; border: 1px solid gray;"> Text text text </div>'.format(b=obj.container_color, t=obj.main_text_color))
    #     if obj.main_text_color:
    #         return mark_safe('<div style="color={t}; height: 25px; width: 100px; border: 1px solid gray;"> Text text text </div>'.format(t=obj.main_text_color))

    def get_home_button_preview(self, obj):
        btn = obj.get_button_style
        mygenricbtn = 'display: inline-block; outline: none; line-height: 40px; padding: 0 30px; font-size: .8em; text-align: center; text-decoration: none; font-weight: 500; cursor: pointer; -webkit-transition: all 0.3s ease 0s; -moz-transition: all 0.3s ease 0s; -o-transition: all 0.3s ease 0s; transition: all 0.3s ease 0s;'

        style = {
            ' e-large': 'padding: 0 40px; line-height: 50px;',
            ' large': 'line-height: 45px;',
            ' medium': 'line-height: 30px;',
            ' small': 'line-height: 25px;',
            'radius': 'border-radius: 3px;',
            'circle': 'border-radius: 20px;',
            'circle arrow': 'border-radius: 20px;',
            'default': 'color: #222; background: #f9f9ff; border: 1px solid transparent;',
            'default-border': 'border: 1px solid #f9f9ff; background: transparent;',
            'primary': 'color: #fff; background: #c6b069; border: 1px solid transparent;',
            'primary-border': 'color: #c6b069; border: 1px solid #c6b069; background: transparent;',
            'success': 'color: #fff; background: #4cd3e3; border: 1px solid transparent;',
            'success-border': 'color: #4cd3e3; border: 1px solid #4cd3e3; background: transparent;',
            'info': 'color: #fff; background: #38a4ff; border: 1px solid transparent;',
            'info-border': 'color: #38a4ff; border: 1px solid #38a4ff; background: transparent;',
            'warning': '  color: #fff; background: #f4e700; border: 1px solid transparent;',
            'warning-border': 'color: #f4e700; border: 1px solid #f4e700; background: transparent;',
            'danger': 'color: #fff; background: #f44a40; border: 1px solid transparent;',
            'danger-border': 'color: #f44a40; border: 1px solid #f44a40; background: transparent;',
            'link': 'color: #222; background: #f9f9ff; text-decoration: underline; border: 1px solid transparent;',
            'link-border': 'color: #222; border: 1px solid #f9f9ff; background: transparent; text-decoration: underline;',
            'disable': 'color: #222,0.3; background: #f9f9ff; border: 1px solid transparent; cursor: not-allowed;',
            None: ' ',
            ' ': ' ',
        }

        color = style[obj.button_color]
        size = style[obj.button_size]
        form = style[obj.button_form]

        return mark_safe('<a href="#" style="{mybtn} {f} {s} {c} text-transform: uppercase; margin-top: 10px"> {t} </a>'.format(mybtn=mygenricbtn, f=form, s=size, c=color, t=obj.home_big_banner_button))

    def preview_container_color(self, obj):
        if obj.container_color:
            return mark_safe('<div style="background-color: {}; height: 25px; width: 100px; border: 1px solid gray;">  </div>'.format(obj.container_color))

    def preview_footer(self, obj):
        if obj.footer_font_color:
            footer_font_color = obj.footer_font_color
        else:
            footer_font_color = obj.main_text_color
        if obj.footer_background_color:
            return mark_safe('<div style="background-color: {b}; color: {t}; height: 25px; width: 100px; border: 1px solid gray;"> Text text text </div>'.format(b=obj.footer_background_color, t=footer_font_color))
        elif obj.background_color:
            return mark_safe('<div style="background-color: {b}; color: {t};  height: 25px; width: 100px; border: 1px solid gray;"> Text text text </div>'.format(b=obj.background_color, t=footer_font_color))

    def preview_vertical_lines_color(self, obj):
        if obj.vertical_lines_color:
            return mark_safe('<div style="background-color: {}; height: 25px; width: 100px; border: 1px solid gray;"> </div>'.format(obj.vertical_lines_color))

    def preview_main_menu_text_color(self, obj):
        if obj.main_menu_text_color:
            main_menu_text_color = obj.main_menu_text_color
        else:
            main_menu_text_color = 'white'
        if obj.overlay_color:
            return mark_safe('<div style="background-color: {b}; color: {t}; height: 25px; width: 100px; border: 1px solid gray;"> Menu Text </div>'.format(b=obj.overlay_color, t=main_menu_text_color))
        else:
            return mark_safe('<div style="background-color: gray; color: {t}; height: 25px; width: 100px; border: 1px solid gray;"> Menu Text </div>'.format(t=main_menu_text_color))

    def preview_overlay(self, obj):
        home_pic = PagePictures.objects.language('en').get(translations__name='home_big_banner_1840x950').image
        banner = PagePictures.objects.language('en').get(translations__name='top_banner_1840x300').image
        if obj.main_menu_text_color:
            main_menu_text_color = obj.main_menu_text_color
        else:
            main_menu_text_color = 'white'
        if home_pic:
            if obj.overlay_color and obj.overlay_opacity:
                fpic = mark_safe('<div style="background: url({im}) no-repeat center center; height: 100px; width: 200px;"><div class="overlay overlay-bg" style="background-color: {b}; color: {t}; opacity: {o}; height: 100px; width: 200px; border: 1px solid gray; color: {t}"> Menu Text </div></div>'.format(im=home_pic.url, b=obj.overlay_color, t=main_menu_text_color, o=obj.overlay_opacity))
            else:
                fpic = mark_safe('<div style="background: url({im}); height: 100px; width: 200px;"><div class="overlay overlay-bg" style="height: 100px; border: 1px solid gray; color: {t}"> Menu Text </div></div>'.format(t=main_menu_text_color, im=home_pic.url, ))
        else:
            if obj.overlay_color and obj.overlay_opacity:
                fpic = mark_safe('<div class="overlay overlay-bg" style="background-color: {b}; color: {t}; opacity: {o}; height: 100px; width: 200px; border: 1px solid gray; color: {t}"> Menu Text </div>'.format(b=obj.overlay_color, t=main_menu_text_color, o=obj.overlay_opacity))
            else:
                fpic = mark_safe('<div class="overlay overlay-bg" style="height: 100px; border: 1px solid gray; color: {t}"> Menu Text </div>'.format(t=main_menu_text_color))
        if banner:
            if obj.overlay_color and obj.overlay_opacity:
                spic = mark_safe('<div style="background: url({im}) no-repeat center center; height: 100px; width: 200px;"><div class="overlay overlay-bg" style="background-color: {b}; color: {t}; opacity: {o}; height: 100px; width: 200px; border: 1px solid gray; color: {t}"> Menu Text </div></div>'.format(im=banner.url, b=obj.overlay_color, t=main_menu_text_color, o=obj.overlay_opacity))
            else:
                spic = mark_safe('<div style="background: url({im}); height: 100px; width: 200px;"><div class="overlay overlay-bg" style="height: 100px; border: 1px solid gray; color: {t}"> Menu Text </div></div>'.format(t=main_menu_text_color, im=banner.url, ))
        else:
            if obj.overlay_color and obj.overlay_opacity:
                spic = mark_safe('<div class="overlay overlay-bg" style="background-color: {b}; color: {t}; opacity: {o}; height: 100px; width: 200px; border: 1px solid gray; color: {t}"> Menu Text </div>'.format(b=obj.overlay_color, t=main_menu_text_color, o=obj.overlay_opacity))
            else:
                spic = mark_safe('<div class="overlay overlay-bg" style="height: 100px; border: 1px solid gray; color: {t}"> Menu Text </div>'.format(t=main_menu_text_color))
        return mark_safe(fpic + '<br>' + spic)

    def get_img_preview(self, obj):
        if obj.background_image.url:
            return mark_safe('<img src="{url}" height=400 />'.format(url=obj.background_image.url))
        else:
            return 'no image'

    def get_logo_preview(self, obj):
        comp = CustomUser.objects.get(username='company')
        if comp.logo:
            if obj.logo_height or obj.logo_width:
                return mark_safe('<img src="{url}" height={h} width={w} />'.format(url=comp.logo.url, h=obj.logo_height, w=obj.logo_width))
            else:
                return mark_safe('<img src="{url}" height=30px width=120px />'.format(url=comp.logo.url))

    def get_font_preview(self, obj):
        a = """
            <link href="https://fonts.googleapis.com/css?family=Poppins:100,200,400,300,500,600,700" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Sriracha&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Lato&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Caveat&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Yanone+Kaffeesatz&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Inconsolata&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Rubik&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Merriweather&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Arizonia&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Marck+Script&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css?family=Poppins:100,200,400,300,500,600,700" rel="stylesheet">
        """
        ttext = a + """
    
            {f}:     <p style="background-color: {c};font-family: {f}; color:{t}">Almost before we knew it, we had left the ground.</p>
        """
        return mark_safe(ttext.format(f=obj.font, t=obj.main_text_color, c=obj.container_color))

    def preview_menu_text_style(self, obj):
        style = obj.get_menu_text_style()
        return mark_safe(mytext.format(style))

    def preview_main_text_style(self, obj):
        style = obj.get_main_text_style()
        return mark_safe(mytext.format(style))

    def preview_big_title_style(self, obj):
        style = obj.get_big_title_style()
        return mark_safe(mytext.format(style))

    def preview_small_title_style(self, obj):
        style = obj.get_small_title_style()
        return mark_safe(mytext.format(style))

    def preview_banner_title_style(self, obj):
        style = obj.get_banner_title_style()
        return mark_safe(mytext.format(style))

    def preview_date_style(self, obj):
        style = obj.get_date_style()
        return mark_safe(mytext.format(style))

    def preview_footer_text_style(self, obj):
        style = obj.get_footer_text_style()
        return mark_safe(mytext.format(style))
