from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

from .models import Project, Profile, News


class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(), label=_('description'))

    class Meta:
        model = Project
        fields = '__all__'


class ProfileAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(), label=_('description'))

    class Meta:
        model = Profile
        fields = '__all__'


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(), label=_('description'))

    class Meta:
        model = News
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label=_('name'))
    email = forms.EmailField(label=_('email'))
    subject = forms.CharField(max_length=50, label=_('subject'))
    message = forms.CharField(label=_('message'))

