import random

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.utils.text import slugify

from design.templatetags import design_tags
from pages.tests import ProjectAndProfileTests
from users.models import CustomUser
from pages.models import Project, Profile, News, Service, ProjectImage, ProjectCategory, ProfileCategory, group
from design.models import DesignSettings, PageTexts, PagePictures


def get_int(c):
    a = str(random.randint(0, 20000))
    while a in c:
        a = str(random.randint(0, 20000))
    c.append(a)
    return a

service_ids = []
news_ids = []
profile_category_ids = []
project_category_ids = []
profile_ids = []
project_ids = []
projectimage_ids = []

short_description_en = 'First phase is a new primary school building, which gives the school compex a new strong defined identity.'
description_en = 'Renovation project for Kuusalu Highschool. First phase is a new primary school building, which gives the school compex a new strong defined identity.' \
                 'Renovation project for Kuusalu Highschool. First phase is a new primary school building, which gives the school compex a new strong defined identity.' \
                 'Renovation project for Kuusalu Highschool. First phase is a new primary school building, which gives the school compex a new strong defined identity.' \
                 'Renovation project for Kuusalu Highschool. First phase is a new primary school building, which gives the school compex a new strong defined identity.' \
                 'Renovation project for Kuusalu Highschool. First phase is a new primary school building, which gives the school compex a new strong defined identity.' \
                 'Renovation project for Kuusalu Highschool. First phase is a new primary school building, which gives the school compex a new strong defined identity.' \

short_description_et = 'Oluline arhitektuurne eesmärk on dialoog uue ja ajaloolise kihistuse vahel. ' \
                       'Juurdeprojekteeritud maastik-ning sisearhitektuursed lahendused on selgelt eristuvad olemasolevast säilitatavast hoonest.'
description_et = 'Arhitektuurse lahenduse lähtepunktiks on luua terviklik ja mitmekülgne õpikeskond, mis võimaldaks ' \
                 'õppetegevust korraldada ühtviisi hästi nii sees kui väljas - neid ühendav spordi ja tegevusrada. Uue lahendusega on eesmärk ' \
                 'elavdada piki koridore liikumist, kujundades voolava ja sportlikuma ruumi. Oluline arhitektuurne eesmärk on dialoog uue ja ajaloolise kihistuse vahel. ' \
                 'Juurdeprojekteeritud maastik-ning sisearhitektuursed lahendused on selgelt eristuvad olemasolevast säilitatavast hoonest.' \
                 'õppetegevust korraldada ühtviisi hästi nii sees kui väljas - neid ühendav spordi ja tegevusrada. Uue lahendusega on eesmärk ' \
                 'elavdada piki koridore liikumist, kujundades voolava ja sportlikuma ruumi. Oluline arhitektuurne eesmärk on dialoog uue ja ajaloolise kihistuse vahel. ' \
                 'Juurdeprojekteeritud maastik-ning sisearhitektuursed lahendused on selgelt eristuvad olemasolevast säilitatavast hoonest.' \
                 'õppetegevust korraldada ühtviisi hästi nii sees kui väljas - neid ühendav spordi ja tegevusrada. Uue lahendusega on eesmärk ' \
                 'elavdada piki koridore liikumist, kujundades voolava ja sportlikuma ruumi. Oluline arhitektuurne eesmärk on dialoog uue ja ajaloolise kihistuse vahel. ' \
                 'Juurdeprojekteeritud maastik-ning sisearhitektuursed lahendused on selgelt eristuvad olemasolevast säilitatavast hoonest.'

short_description_ru = 'Первая фаза - это новое здание начальной школы, которое придает школе новый ярко выраженный облик.'
description_ru = 'Проект реконструкции Куусалуской Высшей Школы. Первая фаза - это новое здание начальной школы, которое придает школе новый ярко выраженный облик.' \
                 'Проект реконструкции Куусалуской Высшей Школы. Первая фаза - это новое здание начальной школы, которое придает школе новый ярко выраженный облик.' \
                 'Проект реконструкции Куусалуской Высшей Школы. Первая фаза - это новое здание начальной школы, которое придает школе новый ярко выраженный облик.' \
                 'Проект реконструкции Куусалуской Высшей Школы. Первая фаза - это новое здание начальной школы, которое придает школе новый ярко выраженный облик.' \
                 'Проект реконструкции Куусалуской Высшей Школы. Первая фаза - это новое здание начальной школы, которое придает школе новый ярко выраженный облик.' \
                 'Проект реконструкции Куусалуской Высшей Школы. Первая фаза - это новое здание начальной школы, которое придает школе новый ярко выраженный облик.' \
                 'Проект реконструкции Куусалуской Высшей Школы. Первая фаза - это новое здание начальной школы, которое придает школе новый ярко выраженный облик.' \
                 'Проект реконструкции Куусалуской Высшей Школы. Первая фаза - это новое здание начальной школы, которое придает школе новый ярко выраженный облик.' \


news_title_en = 'Estonian architecture competition I prize'
news_title_ru = 'Эстонский архитектурный конкурс. 1 место'
news_title_et = 'Eesti arhitektuurivõistluse I koht'


service_title_en = 'Design'
service_title_ru = 'Дизаин'
service_title_et = 'Disain'


profile_category_title_en = 'Manager'
profile_category_title_ru = 'Менеджер'
profile_category_title_et = 'Juhataja'


project_category_title_en = 'Flat'
project_category_title_ru = 'Квартира'
project_category_title_et = 'Korter'


profile_first_name_en = 'Alex'
profile_first_name_ru = 'Алекс'
profile_first_name_et = 'Alex'

profile_last_name_en = 'Argo'
profile_last_name_ru = 'Арго'
profile_last_name_et = 'Argo'

profile_email_en = profile_email_ru = profile_email_et = 'argo@email.com'
profile_facebook_en = profile_facebook_ru = profile_facebook_et = 'fb.com'
profile_twitter_en = profile_twitter_ru = profile_twitter_et = 'twitter.com'
profile_phone_number_en = profile_phone_number_ru = profile_phone_number_et = '+37253402505'

project_title_en = 'project'
project_title_ru = 'проект'
project_title_et = 'projekt'

project_client_en = project_client_ru = project_client_et = 'Admiral OU'
project_website_en = project_website_ru = project_website_et = 'www.vsdemo.ee'
slugen = 'lalala'

# _title_en = ''
# _title_ru = ''
# _title_et = ''


def create_service(a='225'):
    try:
        Service.objects.language('en').get(translations__title=a + service_title_en)
    except ObjectDoesNotExist:
        service = Service.objects.language('en').create(
                title=a + service_title_en,
                short_description=a + short_description_en,
                description=a + description_en,
            )
        service.set_current_language('ru')
        service.title = a + service_title_ru
        service.short_description = a + short_description_ru
        service.description = a + description_ru
        service.slug = slugen + a
        service.save()

        service.set_current_language('et')
        service.title = a + service_title_et
        service.short_description = a + short_description_et
        service.description = a + description_et
        service.slug = slugify(service.title)
        service.save()

        service.set_current_language('en')
        service_ids.append(service.id)


def create_news(a='225'):

    try:
        News.objects.language('en').get(translations__title=a + news_title_en)
    except ObjectDoesNotExist:
        news = News.objects.language('en').create(
                title=a + news_title_en,
                short_description=a + short_description_en,
                description=a + description_en,
            )
        news.set_current_language('ru')
        news.title = a + news_title_ru
        news.short_description = a + short_description_ru
        news.description = a + description_ru
        news.slug = slugen + a
        news.save()

        news.set_current_language('et')
        news.title = a + news_title_et
        news.short_description = a + short_description_et
        news.description = a + description_et
        news.slug = slugify(news.title)
        news.save()

        news.set_current_language('en')
        news_ids.append(news.id)


def create_profileCategory(a='225'):
    try:
        ProfileCategory.objects.language('en').get(translations__title=a + profile_category_title_en)
    except ObjectDoesNotExist:
        category = ProfileCategory.objects.language('en').create(
                title=a + profile_category_title_en,
            )
        category.set_current_language('ru')
        category.title = a + profile_category_title_ru
        category.slug = slugen + a
        category.save()

        category.set_current_language('et')
        category.title = a + profile_category_title_et
        category.slug = slugify(category.title)
        category.save()

        category.set_current_language('en')
        profile_category_ids.append(category.id)


def create_projectCategory(a='225'):
    try:
        ProjectCategory.objects.language('en').get(translations__title=a + project_category_title_en)
    except ObjectDoesNotExist:
        category = ProjectCategory.objects.language('en').create(
                title=a + project_category_title_en,
            )
        category.set_current_language('ru')
        category.title = a + project_category_title_ru
        category.slug = slugify(category.title)
        category.save()

        category.set_current_language('et')
        category.title = a + project_category_title_et
        category.slug = slugify(category.title)

        category.save()

        category.set_current_language('en')
        project_category_ids.append(category.id)


def create_profile(a, oncategory=False):
    # slug = a + profile_first_name_en + profile_last_name_en

    profile = Profile.objects.language('en').get_or_create(
        translations__first_name=a + profile_first_name_en,
        translations__last_name=profile_last_name_en,
        email=profile_email_en,

        facebook=profile_facebook_en,
        twitter=profile_twitter_en,
        phone_number=profile_phone_number_en,
        translations__short_description=a + short_description_en,
        translations__description=a + description_en,

    )
    if oncategory:
        profile.set_current_language('en')
        profile.profile_category.add(ProfileCategory.objects.language('en').first())

    profile.set_current_language('ru')
    profile.translations.first_name = a + profile_first_name_ru
    profile.translations.last_name = a + profile_last_name_ru
    profile.email = profile_email_ru
    profile.facebook = profile_facebook_ru
    profile.twitter = profile_twitter_ru
    profile.phone_number = profile_phone_number_ru
    profile.translations.short_description = a + short_description_ru
    # profile.translations.description = a + description_ru
    profile.slug = slugen + a
    profile.save()

    profile.set_current_language('et')
    profile.translations.first_name = a + profile_first_name_et
    profile.translations.last_name = a + profile_last_name_et
    profile.email = profile_email_et
    profile.facebook = profile_facebook_et
    profile.twitter = profile_twitter_et
    profile.phone_number = profile_phone_number_et
    profile.translations.short_description = a + short_description_et
    # profile.translations.description = a + description_et
    profile.slug = slugify(profile.get_name())
    profile.save()

    profile.set_current_language('en')
    profile_ids.append(profile.id)


def create_project(oncategory=False, a='225'):
    try:
        Project.objects.language('en').get_or_create(translations__slug=a + project_title_en)
    except ObjectDoesNotExist:
        project = Project.objects.language('en').create(
            title=a + project_title_en,
            client=a + project_client_en,
            website=project_website_en,
            short_description=a + short_description_en,
            description=a + description_en,
        )

        if oncategory:
            project.set_current_language('en')
            project.project_category.add(ProjectCategory.objects.language('en').first())

        project.set_current_language('ru')
        project.title = a + project_title_ru
        project.client = a + project_client_ru
        project.website = project_website_ru
        project.short_description = a + short_description_ru
        project.description = a + description_ru
        project.slug = slugen + a
        project.save()

        project.set_current_language('et')
        project.title = a + project_title_et
        project.client = a + project_client_et
        project.website = project_website_et
        project.short_description = a + short_description_et
        project.description = a + description_et
        project.slug = slugify(project.title)
        project.save()

        project.set_current_language('en')
        project_ids.append(project.id)


def create_project_image(project):
    img = ProjectImage.objects.get_or_create(project=project, image='images/defaults/project-details.jpg')[0]
    projectimage_ids.append(img.id)


def create_test_data(request):
    #
    # user = get_user_model().objects.create_user(
    #     username='company',
    #     email='company@email.com',
    #     password='testpass123'
    # )

    profile_category_designer = ProfileCategory.objects.create(
        title='Designer',
    )

    profile_category_manager = ProfileCategory.objects.create(
        title='Manager',
    )

    profile = Profile.objects.create(
        first_name='Alex',
        last_name='Argo',
        email='argo@email.com',

        facebook='fb.com',
        twitter='twitter.com',
        phone_number='+37253402505',
        short_description='hejhej lala lej',
        description='description description',
    )

    profile2 = Profile.objects.create(
        first_name='Lara',
        last_name='Mara',
        email='lama@email.com',
        short_description='kuku jamba'
    )

    project = Project.objects.create(
        title='Django site',
        short_description='lalala',
    )

    project2 = Project.objects.create(
        title='JavaScript site',
        short_description='hehehe',
    )

    project_category_python = ProjectCategory.objects.create(
        title='Python',
    )

    project_category_js = ProjectCategory.objects.create(
        title='JS',
    )

    design = DesignSettings.objects.create(
        info='default'
    )

    project.save()
    project2.save()
    profile.save()
    profile2.save()

    # self.project_category_python = ProjectCategory.objects.active_translations(language_code='en', title='Python').first()
    # self.project_category_js = ProjectCategory.objects.active_translations(language_code='en', title='JS').first()

    # self.profile_category_manager = ProfileCategory.objects.active_translations(language_code='en', title='Manager').first()
    # self.profile_category_designer = ProfileCategory.objects.active_translations(language_code='en', title='Designer').first()
    #
    # self.first_profile = Profile.objects.active_translations(language_code='en', id=self.profile.id).first()
    # self.second_profile = Profile.objects.active_translations(language_code='en', id=self.profile2.id).first()

    project.project_category.add(project_category_python)
    project.project_team.add(profile)

    project2.project_category.add(project_category_python, project_category_js)
    project2.project_team.add(profile, profile2)

    profile.profile_category.add(profile_category_manager, profile_category_designer)
    profile2.profile_category.add(profile_category_designer)

    # self.review = Review.objects.create(
    #     book=self.book,
    #     author=self.user,
    #     review='An excellent review',
    # )

    # for n in range(0, 10):
    #     g = 'o4' + str(n)
    #     create_service(a=g)
    #     create_profileCategory(a=g)
    #     create_projectCategory(a=g)
    #
    #     create_profile(a=g)
    #     create_news(a=g)
    #     create_project(a=g)
    #
    #     h = 'cat' + g
    #     create_profile(a=h, oncategory=True)
    #     create_project(a=h, oncategory=True)
    #
    # for n in range(0, 4):
    #     for proj in Project.objects.language('en').all():
    #         create_project_image(proj)

    return redirect('pages:home')


def delete_all_data(request):
    service_ids.clear()
    news_ids.clear()
    profile_category_ids.clear()
    project_category_ids.clear()
    profile_ids.clear()
    project_ids.clear()
    projectimage_ids.clear()

    News.objects.all().delete()
    Service.objects.all().delete()
    ProfileCategory.objects.all().delete()
    ProjectCategory.objects.all().delete()
    Profile.objects.all().delete()
    Project.objects.all().delete()
    ProjectImage.objects.all().delete()

    return redirect('pages:home')


def delete_test_data(request):
    Service.objects.filter(id__in=service_ids).delete()
    News.objects.filter(id__in=news_ids).delete()
    ProfileCategory.objects.filter(id__in=profile_category_ids).delete()
    ProjectCategory.objects.filter(id__in=project_category_ids).delete()
    Profile.objects.filter(id__in=profile_ids).delete()
    Project.objects.filter(id__in=project_ids).delete()
    ProjectImage.objects.filter(id__in=projectimage_ids).delete()

    service_ids.clear()
    news_ids.clear()
    profile_category_ids.clear()
    project_category_ids.clear()
    profile_ids.clear()
    project_ids.clear()
    projectimage_ids.clear()
    return redirect('pages:home')


def delete_all_data(request):
    Service.objects.all().delete()
    News.objects.all().delete()
    ProfileCategory.objects.all().delete()
    ProjectCategory.objects.all().delete()
    Profile.objects.all().delete()
    Project.objects.all().delete()
    ProjectImage.objects.all().delete()

    CustomUser.objects.exclude(username='admin').delete()

    DesignSettings.objects.all().delete()
    PageTexts.objects.all().delete()
    PagePictures.objects.all().delete()

    service_ids.clear()
    news_ids.clear()
    profile_category_ids.clear()
    project_category_ids.clear()
    profile_ids.clear()
    project_ids.clear()
    projectimage_ids.clear()

    DesignSettings.objects.language('en').create(info='default')
    password = CustomUser.objects.make_random_password()
    CustomUser.objects.create(username='company', password=password)

    design_tags.about_texts()
    design_tags.project_list_texts()
    design_tags.project_detail_texts()
    design_tags.people_list_texts()
    design_tags.profile_texts()
    design_tags.service_list_texts()
    design_tags.service_detail_texts()
    design_tags.news_detail_texts()
    design_tags.news_list_texts()
    design_tags.about_texts()
    design_tags.contact_texts()
    design_tags.success_texts()
    design_tags.home_callto_texts()
    design_tags.footer_texts()
    design_tags.home_big_banner()
    design_tags.top_banner_1840x300()
    design_tags.home_call_to_banner_1110x350()
    design_tags.category_settings()
    design_tags.contact_form_tag()
    return redirect('pages:home')