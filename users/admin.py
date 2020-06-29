from django.contrib.admin import ModelAdmin
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

CustomUser = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    save_on_top = True
    model = CustomUser
    list_display = [
        'username',
        'company_name',
        'email', 'phone_number',
    ]
    readonly_fields = ['get_logo_preview', ]
    fieldsets = [
        (None, {
            'fields': (('username', 'first_name', 'last_name'), 'active', 'is_staff', 'groups', )
        }),
        (_('Address'), {
            'fields': ('address', 'postal_code', 'city', 'country')
        }),
        (_('Company'), {
            'fields': ('company_name', 'registation_number', 'address_inline',)
        }),
        (_('Contact'), {
            "fields": ('email', 'phone_number', 'time_for_colling')
        }),
        (_('Follow Us'), {
            "fields": ('facebook', 'instagram', 'twitter')
        }),
        (_('Password'), {
            'fields': ('password', )
        }),
        (_('Logo'), {
            'fields': ('logo', 'get_logo_preview', )
        }),
    ]

    # def has_delete_permission(self, request, obj=None):
    #     #Disable delete
    #     return False
    #
    # def has_add_permission(self, request):
    #     #Disable add
    #     return False
    #

    def get_logo_preview(self, obj):
        return mark_safe('<img src="{url}" width=120 height=30 style="background-color: lightslategray"/>'.format(url=obj.logo.url))

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            self.readonly_fields.append('is_staff')
            self.readonly_fields.append('groups')
        return self.readonly_fields