import datetime

from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import ContactForm
from .models import Project, ProjectCategory, Profile, Service, ProfileCategory, News
from .views import HomePageView, AboutView, ContactView, SuccessView


# setUpTestData


class HomepageTests(TestCase):

    def setUp(self):
        url = reverse('pages:home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'pages/home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Home')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/en/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(TestCase):

    def setUp(self):
        url = reverse('pages:about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'pages/about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Us')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_aboutpage_url_resolves_aboutview(self):
        view = resolve('/en/about_us/')
        self.assertEqual(view.func.__name__, AboutView.as_view().__name__)


class ProjectAndProfileTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='company',
            email='company@email.com',
            password='testpass123'
        )

        self.profile_category = ProfileCategory.objects.create(
            title='Designer',
        )

        self.profile_category2 = ProfileCategory.objects.create(
            title='Manager',
        )

        self.profile = Profile.objects.create(
            first_name='Alex',
            last_name='Argo',
            email='argo@email.com',

            facebook='fb.com',
            twitter='twitter.com',
            phone_number='+37253402505',
            short_description='hejhej lala lej',
            description='description description',
        )

        self.profile2 = Profile.objects.create(
            first_name='Lara',
            last_name='Mara',
            email='lama@email.com',
            short_description='kuku jamba'
        )

        self.project = Project.objects.create(
            title='Django site',
            short_description='lalala',
        )

        self.project2 = Project.objects.create(
            title='JS site',
            short_description='hehehe',
        )

        self.project_category = ProjectCategory.objects.create(
            title='Python',
        )

        self.project_category2 = ProjectCategory.objects.create(
            title='JS',
        )
        self.fc = ProjectCategory.objects.active_translations(language_code='en', title='Python').first()
        self.project.project_category.add(self.fc)
        self.fp = Profile.objects.active_translations(language_code='en', id=self.profile.id).first()
        self.project.project_team.add(self.fp)
        #
        # self.project2.project_category.add(ProjectCategory.objects.get(title='JS'), ProjectCategory.objects.get(title='Python'))
        # self.project2.project_team.add(Profile.objects.get(id=self.profile.id), Profile.objects.get(id=self.profile2.id))
        #
        # self.profile.profile_category.add(ProfileCategory.objects.get(title='Manager'), ProfileCategory.objects.get(title='Designer'))
        # self.profile2.profile_category.add(ProfileCategory.objects.get(title='Designer'))

        # self.review = Review.objects.create(
        #     book=self.book,
        #     author=self.user,
        #     review='An excellent review',
        # )

    def test_project_listing(self):
        project_team = self.project.project_team.first()
        project_category = self.project.project_category.first()

        self.assertEqual(f'{self.project.safe_translation_getter("title", language_code="en")}', 'Django site')
        self.assertEqual(f'{project_category.safe_translation_getter("title", language_code="en")}', 'Python')
        self.assertEqual(f'{project_team.get_name()}', 'Alex Argo')
        self.assertEqual(f'{self.project.safe_translation_getter("short_description", language_code="en")}', 'lalala')

#     def test_project2_listing(self):
#         project_team = self.project2.project_team.all().order_by('first_name')
#         project_category = self.project2.project_category.all().order_by('title')
#
#         self.assertEqual(f'{self.project2.title}', 'JS site')
#         self.assertEqual(f'{project_category[1].title}', 'Python')
#         self.assertEqual(f'{project_category[0].title}', 'JS')
#         self.assertEqual(f'{project_team[1].get_name()}', 'Lara Mara')
#         self.assertEqual(f'{project_team[0].get_name()}', 'Alex Argo')
#         self.assertEqual(f'{self.project2.short_description}', 'hehehe')
#
#     def test_project_list_view(self):
#         response = self.client.get(reverse('pages:projects'))
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Django site')
#         self.assertTemplateUsed(response, 'pages/projects_list.html')
#
#     def test_category_project_list_view(self):
#         response = self.client.get(reverse('pages:projects_category', kwargs={'category_slug': 'js'}))
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'JS site')
#         self.assertNotContains(response, 'Django site')
#         self.assertTemplateUsed(response, 'pages/projects_list.html')
#
#     def test_category2_project_list_view(self):
#         response = self.client.get(reverse('pages:projects_category', kwargs={'category_slug': 'python'}))
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'JS site')
#         self.assertContains(response, 'Django site')
#         self.assertTemplateUsed(response, 'pages/projects_list.html')
#
#     def test_project_detail_view(self):
#         response = self.client.get(self.project.get_absolute_url())
#         no_response = self.client.get('/en/projects/12345/')
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, 'Django site')
#         self.assertContains(response, 'lalala')
#         self.assertContains(response, 'Alex Argo')
#         self.assertContains(response, 'Python')
#         self.assertNotContains(response, 'Lara Mara')
#         self.assertNotContains(response, 'hehehe')
#         self.assertTemplateUsed(response, 'pages/project_detail.html')
#
#     def test_project2_detail_view(self):
#         response = self.client.get(self.project2.get_absolute_url())
#         no_response = self.client.get('/en/projects/12345/')
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, 'JS site')
#         self.assertContains(response, 'hehehe')
#         self.assertContains(response, 'Lara Mara')
#         self.assertContains(response, 'JS')
#         self.assertContains(response, 'Alex Argo')
#         self.assertContains(response, 'Python')
#         self.assertTemplateUsed(response, 'pages/project_detail.html')
#
#     # profile
#     def test_profile2_listing(self):
#         projects = self.profile2.projects.first()
#         profile_category = self.profile2.profile_category.first()
#
#         self.assertEqual(f'{self.profile2.get_name()}', 'Lara Mara')
#         self.assertEqual(f'{profile_category.title}', 'Designer')
#         self.assertEqual(f'{projects.title}', 'JS site')
#         self.assertEqual(f'{projects.short_description}', 'hehehe')
#
#     def test_profile_listing(self):
#         projects = self.profile.projects.all().order_by('title')
#         profile_categories = self.profile.profile_category.all().order_by('title')
#
#         self.assertEqual(f'{self.profile.get_name()}', 'Alex Argo')
#         self.assertEqual(f'{profile_categories[0].title}', 'Designer')
#         self.assertEqual(f'{profile_categories[1].title}', 'Manager')
#         self.assertEqual(f'{projects[0].title}', 'Django site')
#         self.assertEqual(f'{projects[1].title}', 'JS site')
#         self.assertEqual(f'{projects[1].short_description}', 'hehehe')
#
#     def test_profile_list_view(self):
#         response = self.client.get(reverse('pages:people'))
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Alex Argo')
#         self.assertContains(response, 'Lara Mara')
#         self.assertContains(response, 'Designer')
#         self.assertContains(response, 'Manager')
#         self.assertNotContains(response, 'hejhej lala lej')
#         self.assertNotContains(response, 'kuku jamba')
#         self.assertTemplateUsed(response, 'pages/people_list.html')
#
#     def test_profile_category_list_view(self):
#         response = self.client.get(reverse('pages:profile_category', kwargs={'category_slug': 'manager'}))
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Alex Argo')
#         self.assertNotContains(response, 'Lara Mara')
#         self.assertContains(response, 'Designer')
#         self.assertContains(response, 'Manager')
#         self.assertTemplateUsed(response, 'pages/people_list.html')
#
#     def test_profile_category2_list_view(self):
#         response = self.client.get(reverse('pages:profile_category', kwargs={'category_slug': 'designer'}))
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Alex Argo')
#         self.assertContains(response, 'Lara Mara')
#         self.assertContains(response, 'Designer')
#         self.assertContains(response, 'Manager')
#         self.assertTemplateUsed(response, 'pages/people_list.html')
#
#     def test_profile_detail_view(self):
#         response = self.client.get(self.profile.get_absolute_url())
#         no_response = self.client.get('/en/people/12345/')
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, 'Alex Argo')
#         self.assertContains(response, 'argo@email.com')
#         self.assertContains(response, 'fb.com')
#         self.assertContains(response, 'twitter.com')
#         self.assertContains(response, '+37253402505')
#         self.assertContains(response, 'hejhej lala lej')
#         self.assertContains(response, 'description description')
#         self.assertNotContains(response, 'Lara Mara')
#         self.assertNotContains(response, 'hehehe')
#         self.assertTemplateUsed(response, 'pages/profile.html')
#
#     def test_profile2_detail_view(self):
#         response = self.client.get(self.profile2.get_absolute_url())
#         no_response = self.client.get('/en/profile/12345/')
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, 'Lara Mara')
#         self.assertContains(response, 'lama@email.com')
#         self.assertContains(response, 'kuku jamba')
#         self.assertNotContains(response, 'twitter')
#
#         self.assertTemplateUsed(response, 'pages/profile.html')
#
#
# class ServiceTests(TestCase):
#
#     def setUp(self):
#         self.service = Service.objects.create(
#             title='design',
#             short_description='short_description',
#             description='descriptiondescription descriptiondescription',
#         )
#
#     def test_service_listing(self):
#
#         self.assertEqual(f'{self.service.title}', 'design')
#         self.assertEqual(f'{self.service.short_description}', 'short_description')
#         self.assertEqual(f'{self.service.description}', 'descriptiondescription descriptiondescription')
#
#     def test_service_list_view(self):
#         response = self.client.get(reverse('pages:service_list'))
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'short_description')
#         self.assertNotContains(response, 'descriptiondescription descriptiondescription')
#         self.assertTemplateUsed(response, 'pages/service_list.html')
#
#     def test_service_detail_view(self):
#         response = self.client.get(self.service.get_absolute_url())
#         no_response = self.client.get('/en/service/12345/')
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, 'design')
#         self.assertContains(response, 'short')
#         self.assertContains(response, 'description')
#         self.assertTemplateUsed(response, 'pages/service_detail.html')
#
#
# class NewsTests(TestCase):
#
#     def setUp(self):
#         self.news = News.objects.create(
#             title='Monday',
#             short_description='short_description',
#             description='descriptiondescription descriptiondescription',
#         )
#
#     def test_news_listing(self):
#
#         self.assertEqual(f'{self.news.title}', 'Monday')
#         self.assertEqual(f'{self.news.short_description}', 'short_description')
#         self.assertEqual(f'{self.news.description}', 'descriptiondescription descriptiondescription')
#
#     def test_news_list_view(self):
#         response = self.client.get(reverse('pages:news'))
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'short_description')
#         self.assertNotContains(response, 'descriptiondescription descriptiondescription')
#         self.assertTemplateUsed(response, 'pages/news_list.html')
#
#     def test_news_detail_view(self):
#         response = self.client.get(self.news.get_absolute_url())
#         no_response = self.client.get('/en/news/12345/')
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, 'Monday')
#         self.assertContains(response, 'short')
#         self.assertContains(response, 'description')
#         self.assertContains(response, datetime.date.today().year)
#         self.assertTemplateUsed(response, 'pages/news_detail.html')
#
#
# class ContactTests(TestCase):
#
#     def setUp(self):
#         url = reverse('pages:contact')
#         self.response = self.client.get(url)
#
#     def test_contactpage_status_code(self):
#         self.assertEqual(self.response.status_code, 200)
#
#     def test_contactpage_template(self):
#         self.assertTemplateUsed(self.response, 'pages/contact.html')
#
#     def test_contactpage_contains_correct_html(self):
#         self.assertContains(self.response, 'Contact Us')
#
#     def test_contactpage_does_not_contain_incorrect_html(self):
#         self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
#
#     def test_contactpage_url_resolves_contactpageview(self):
#         view = resolve('/contact/')
#         self.assertEqual(view.func.__name__, ContactView.as_view().__name__)
#
#     def test_form(self):
#         data = {
#             'name': 'Vasja',
#             'email': 'admin@admin.ee',
#             'subject': 'LALALA',
#             'message': 'textetxtext text text',
#         }
#
#         ContactView.send_email(ContactView.as_view(), data)
#         with self.settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'):
#             self.assertEqual(len(mail.outbox), 1)
#             self.assertEqual(mail.outbox[0].subject, 'Vasja LALALA')
#
#
# class ContactSuccessTests(TestCase):
#
#     def setUp(self):
#         url = reverse('pages:success')
#         self.response = self.client.get(url)
#
#     def test_contactsuccesspage_status_code(self):
#         self.assertEqual(self.response.status_code, 200)
#
#     def test_contactsuccesspage_template(self):
#         self.assertTemplateUsed(self.response, 'pages/success.html')
#
#     def test_contactsuccesspage_contains_correct_html(self):
#         self.assertContains(self.response, 'Success')
#
#     def test_contactsuccesspage_does_not_contain_incorrect_html(self):
#         self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
#
#     def test_contactsuccesspage_url_resolves_homepageview(self):
#         view = resolve('/contact/success/')
#         self.assertEqual(view.func.__name__, SuccessView.as_view().__name__)
#
#
# class AddCompanyDataTests(TestCase):
#     pass