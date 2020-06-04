from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin
from parler.forms import TranslatableModelForm, TranslatedField
from parler.models import TranslatedFields

from .models import PageTexts


class PageTextsAdminForm(TranslatableModelForm):
    big_page_title = forms.CharField(label=_('big page title'), widget=CKEditorUploadingWidget()),
    small_page_title = forms.CharField(label=_('small page title'), widget=CKEditorUploadingWidget()),

    translations = TranslatedFields(
        big_page_title=forms.CharField(label=_('big page title'), widget=CKEditorUploadingWidget()),
        small_page_title=forms.CharField(label=_('small page title'), widget=CKEditorUploadingWidget()),
    )

    class Meta:
        model = PageTexts
        exclude = ('name', )

