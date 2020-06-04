from django import template
from django.core.exceptions import ObjectDoesNotExist
from parler.utils.context import switch_language

from texts.models import PageTexts

register = template.Library()


@register.simple_tag(name='try_texts')
def try_texts():
    try:
        PageTexts.objects.language('en').get(translations__name='home_texts')
        return True
    except:
        return False

@register.simple_tag(name='home_texts')
def home_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='home_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(name='home_texts')
        page.set_current_language('ru')
        page.name = 'главная_тексты'
        page.save()
    return page


@register.simple_tag(name='project_list_texts')
def project_list_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='project_list_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(name='project_list_texts')
        page.set_current_language('ru')
        page.name = 'список_проектов_тексты'
        page.save()
    return page


@register.simple_tag(name='project_detail_texts')
def project_detail_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='project_detail_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(name='project_detail_texts')
        page.set_current_language('ru')
        page.name = 'проект_тексты'
        page.save()
    return page


@register.simple_tag(name='people_list_texts')
def people_list_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='people_list_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(name='people_list_texts')
        page.set_current_language('ru')
        page.name = 'список_людей_тексты'
        page.save()
    return page


@register.simple_tag(name='profile_texts')
def profile_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='profile_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(name='profile_texts')
        page.set_current_language('ru')
        page.name = 'профиль_тексты'
        page.save()
    return page


@register.simple_tag(name='service_list_texts')
def service_list_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='service_list_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(name='service_list_texts')
        page.set_current_language('ru')
        page.name = 'список_сервисов_тексты'
        page.save()
    return page


@register.simple_tag(name='service_detail_texts')
def service_detail_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='service_detail_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(name='service_detail_texts')
        page.set_current_language('ru')
        page.name = 'сервис_тексты'
        page.save()
    return page


@register.simple_tag(name='news_detail_texts')
def news_detail_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='news_detail_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(name='news_detail_texts')
        page.set_current_language('ru')
        page.name = 'список_новостей_тексты'
        page.save()
    return page


@register.simple_tag(name='news_list_texts')
def news_list_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='news_list_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(name='news_list_texts')
        page.set_current_language('ru')
        page.name = 'новость_тексты'
        page.save()
    return page


@register.simple_tag(name='about_texts')
def about_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='about_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(name='about_texts')
        page.set_current_language('ru')
        page.name = 'о_нас_тексты'
        page.save()
    return page


@register.simple_tag(name='contact_texts')
def contact_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='contact_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(name='contact_texts')
        page.set_current_language('ru')
        page.name = 'контакты_тексты'
        page.save()
    return page
