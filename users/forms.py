from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from users.models import CustomUser


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=('Password'), help_text=("<a href=\"{% url 'auth:set_password' %}\"> change <\\a> "))

    class Meta:
        model = CustomUser
        fields = ('password', )

