from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

CustomUser = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    save_on_top = True
    model = CustomUser
    list_display = [
        'username', 'first_name', 'last_name',
        'company_name',
        'email', 'phone_number',
    ]
    fieldsets = [
        (None, {
            'fields': (('username', 'first_name', 'last_name'), 'active')
        }),
        (_('Address'), {
            'fields': ('address', 'postal_code', 'city', 'country')
        }),
        (_('Company'), {
            'fields': ('company_name', 'registation_number', 'address_inline', 'languages',)
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
            'fields': ('logo',)
        }),
    ]





