from django import template
from django.core.exceptions import ObjectDoesNotExist
from parler.utils.context import switch_language

from texts.models import PageTexts, PagePictures

register = template.Library()


@register.simple_tag(name='try_texts')
def try_texts():
    try:
        PageTexts.objects.language('en').get(translations__name='footer_texts')
        return True
    except:
        return False


@register.simple_tag(name='home_texts')
def home_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='home_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='home_texts',
            big_page_title='Big page title home_texts',
            small_page_title='Small page title home_texts',
        )
        page.set_current_language('ru')
        page.name = 'домашняя_страница_тексты'
        page.set_current_language('et')
        page.name = 'avaleht_tekst'
        page.save()
    return page


@register.simple_tag(name='project_list_texts')
def project_list_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='project_list_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='project_list_texts',
            big_page_title='Big page title project_list_texts',
            small_page_title='Small page title project_list_texts',
        )
        page.set_current_language('ru')
        page.name = 'список_проектов_тексты'
        page.set_current_language('et')
        page.name = 'project_nimikiri_tekst'
        page.save()
    return page


@register.simple_tag(name='project_detail_texts')
def project_detail_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='project_detail_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='project_detail_texts',
            big_page_title='Big page title project_detail_texts',
            small_page_title='Small page title project_detail_texts',
        )
        page.set_current_language('ru')
        page.name = 'проект_тексты'
        page.set_current_language('et')
        page.name = 'projekt_detailid_tekst'
        page.save()
    return page


@register.simple_tag(name='people_list_texts')
def people_list_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='people_list_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='people_list_texts',
            big_page_title='Big page title people_list_texts',
            small_page_title='Small page title people_list_texts',
        )
        page.set_current_language('ru')
        page.name = 'список_людей_тексты'
        page.set_current_language('et')
        page.name = 'inimesed_nimikiri_tekst'
        page.save()
    return page


@register.simple_tag(name='profile_texts')
def profile_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='profile_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='profile_texts',
            big_page_title='Big page title profile_texts',
            small_page_title='Small page title profile_texts',
        )
        page.set_current_language('ru')
        page.name = 'профиль_тексты'
        page.set_current_language('et')
        page.name = 'profiil_tekst'
        page.save()
    return page


@register.simple_tag(name='service_list_texts')
def service_list_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='service_list_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='service_list_texts',
            big_page_title='Big page title service_list_texts',
            small_page_title='Small page title service_list_texts',
        )
        page.set_current_language('ru')
        page.name = 'список_сервисов_тексты'
        page.set_current_language('et')
        page.name = 'teenused_nimikiri_tekst'
        page.save()
    return page


@register.simple_tag(name='service_detail_texts')
def service_detail_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='service_detail_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='service_detail_texts',
            big_page_title='Big page title service_detail_texts',
            small_page_title='Small page title service_detail_texts',
        )
        page.set_current_language('ru')
        page.name = 'сервис_тексты'
        page.set_current_language('et')
        page.name = 'teenused_detailid_tekst'
        page.save()
    return page


@register.simple_tag(name='news_detail_texts')
def news_detail_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='news_detail_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='news_detail_texts',
            big_page_title='Big page title news_detail_texts',
            small_page_title='Small page title news_detail_texts',
        )
        page.set_current_language('ru')
        page.name = 'список_новостей_тексты'
        page.set_current_language('et')
        page.name = 'uudised_detailid_tekst'
        page.save()
    return page


@register.simple_tag(name='news_list_texts')
def news_list_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='news_list_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='news_list_texts',
            big_page_title='Big page title news_list_texts',
            small_page_title='Small page title news_list_texts',
        )
        page.set_current_language('ru')
        page.name = 'новость_тексты'
        page.set_current_language('et')
        page.name = 'uudised_nimikiri_tekst'
        page.save()
    return page


@register.simple_tag(name='about_texts')
def about_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='about_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='about_texts',
            big_page_title='Big page title about_texts',
            small_page_title='Small page title about_texts',
        )
        page.set_current_language('ru')
        page.name = 'о_нас_тексты'
        page.set_current_language('et')
        page.name = 'meist_tekst'
        page.save()
    return page


@register.simple_tag(name='contact_texts')
def contact_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='contact_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='contact_texts',
            big_page_title='Big page title contact_texts',
            small_page_title='Small page title contact_texts',
        )
        page.set_current_language('ru')
        page.name = 'контакты_тексты'
        page.set_current_language('et')
        page.name = 'kontakt_tekst'
        page.save()
    return page


@register.simple_tag(name='success_texts')
def success_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='success_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='success_texts',
            big_page_title='Big page title success_texts',
            small_page_title='Small page title success_texts',
        )
        page.set_current_language('ru')
        page.name = 'успех_тексты'
        page.set_current_language('et')
        page.name = 'edu_tekst'
        page.save()
    return page


@register.simple_tag(name='home_callto_texts')
def home_callto_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='home_callto_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='home_callto_texts',
            big_page_title='Big page title home_callto_texts',
            small_page_title='Small page title home_callto_texts',
        )

        page.set_current_language('ru')
        page.name = 'главная_callto_тексты'
        page.set_current_language('et')
        page.name = 'avaleht_callto_tekst'
        page.save()
    return page


@register.simple_tag(name='footer_texts')
def footer_texts():
    try:
        page = PageTexts.objects.language('en').get(translations__name='footer_texts')
    except ObjectDoesNotExist:
        page = PageTexts.objects.language('en').create(
            name='footer_texts',
            big_page_title='Big page title footer_texts',
            small_page_title='Small page title footer_texts',
        )
        page.set_current_language('ru')
        page.name = 'низ_тексты'
        page.set_current_language('et')
        page.name = 'footer_tekst'

        page.save()
    return page


@register.simple_tag(name='home_big_banner_1840x950')
def home_big_banner():
    try:
        picture = PagePictures.objects.language('en').get(translations__name='home_big_banner_1840x950')
    except ObjectDoesNotExist:
        picture = PagePictures.objects.language('en').create(
            name='home_big_banner_1840x950',
        )
        picture.set_current_language('ru')
        picture.name = 'домашняя_большой_баннер_1840x950'
        picture.set_current_language('et')
        picture.name = 'avaleht_suur_banner_1840x950'

        picture.save()
    return picture


@register.simple_tag(name='top_banner_1840x300')
def top_banner_1840x300():
    try:
        picture = PagePictures.objects.language('en').get(translations__name='top_banner_1840x300')
    except ObjectDoesNotExist:
        picture = PagePictures.objects.language('en').create(
            name='top_banner_1840x300',
        )
        picture.set_current_language('ru')
        picture.name = 'верхний_баннер_1840x300'
        picture.set_current_language('et')
        picture.name = 'ulaosa_banner_1840x300'

        picture.save()
    return picture


@register.simple_tag(name='home_call_to_banner_1110x350')
def home_call_to_banner_1110x350():
    try:
        picture = PagePictures.objects.language('en').get(translations__name='home_call_to_banner_1110x350')
    except ObjectDoesNotExist:
        picture = PagePictures.objects.language('en').create(
            name='home_call_to_banner_1110x350',
        )
        picture.set_current_language('ru')
        picture.name = 'домашняя_call_to_баннер_1110x350'
        picture.set_current_language('et')
        picture.name = 'avaleht_call_to_banner_1110x350'

        picture.save()
    return picture

