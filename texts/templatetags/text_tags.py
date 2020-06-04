from django import template
from django.core.exceptions import ObjectDoesNotExist

from texts.models import PageTexts

register = template.Library()


@register.simple_tag(name='contact_texts')
def contact_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='contact_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(name='contact_texts')
    return page
