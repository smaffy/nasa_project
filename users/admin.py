from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

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
        ('Address', {
            'fields': ('address', 'postal_code', 'city', 'country')
        }),
        ('Company', {
            'fields': ('company_name',)
        }),
        ('Contact', {
            "fields": ('email', 'phone_number', 'time_for_colling')
        }),
        ('Follow Us', {
            "fields": ('facebook', 'instagram', 'twitter')
        }),
        ('Password', {
            'fields': ('password', )
        }),
    ]





