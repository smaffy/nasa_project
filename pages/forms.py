from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin
from parler.forms import TranslatableModelForm, TranslatedField
from parler.models import TranslatedFields

from .models import Project, Profile, News


class ProjectAdminForm(TranslatableModelForm):
    title = forms.CharField(label=_('title'), max_length=200)
    slug = forms.SlugField(label=_('slug'), max_length=200)
    short_description = forms.CharField(label=_('short_description'), max_length=5000)
    description = forms.CharField(widget=CKEditorUploadingWidget(), label=_('description'))

    translations = TranslatedFields(
        title=forms.CharField(label=_('title'), max_length=200),
        slug=forms.SlugField(label=_('slug'), max_length=200),
        short_description=forms.CharField(label=_('short_description'), max_length=5000),
        description=forms.CharField(widget=CKEditorUploadingWidget(), label=_('description'))
    )

    class Meta:
        model = Project
        fields = '__all__'


class ProfileAdminForm(TranslatableModelForm):
    first_name = forms.CharField(label=_('first name'), max_length=200)
    last_name = forms.CharField(label=_('first name'), max_length=200)
    slug = forms.SlugField(label=_('slug'), max_length=200)
    short_description = forms.CharField(label=_('short_description'), max_length=5000)
    description = forms.CharField(widget=CKEditorUploadingWidget(), label=_('description'))

    translations = TranslatedFields(
        first_name=forms.CharField(label=_('first name'), max_length=200),
        last_name = forms.CharField(label=_('first name'), max_length=200),
        slug=forms.SlugField(label=_('slug'), max_length=200),
        short_description=forms.CharField(label=_('short_description'), max_length=5000),
        description=forms.CharField(widget=CKEditorUploadingWidget(), label=_('description'))
    )

    class Meta:
        model = Profile
        fields = '__all__'


class NewsAdminForm(ProjectAdminForm):
    class Meta:
        model = News
        fields = '__all__'
    # def __init__(self, *args, **kwargs):
    #     super(NewsAdminForm, self).__init__(*args, **kwargs)
    #     self.fields['some_field'].queryset = self.fields['some_field'].queryset.prefetch_related('translations')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label=_('name'))
    email = forms.EmailField(label=_('email'))
    subject = forms.CharField(max_length=50, label=_('subject'))
    message = forms.CharField(label=_('message'))

