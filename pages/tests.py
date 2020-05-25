from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .models import Project, ProjectCategory, Profile
from .views import HomePageView, AboutView

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
        view = resolve('/')
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
        view = resolve('/about_us/')
        self.assertEqual(view.func.__name__, AboutView.as_view().__name__)


class ProjectTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='company',
            email='company@email.com',
            password='testpass123'
        )

        self.profile = Profile.objects.create(
            first_name='Alex',
            last_name='Argo',
            email='argo@email.com',
            short_description='hejhej lala lej'
        )

        self.project_category = ProjectCategory.objects.create(
            title='Python',
        )

        self.project = Project.objects.create(
            title='Python/Django site',
            short_description='lalala',
        )
        self.project.project_category.add(ProjectCategory.objects.get(title='Python'))
        self.project.project_team.add(Profile.objects.get(id=self.profile.id))


        # self.review = Review.objects.create(
        #     book=self.book,
        #     author=self.user,
        #     review='An excellent review',
        # )

    def test_book_listing(self):
        project_team = self.project.project_team.first()
        project_category = self.project.project_category.first()

        self.assertEqual(f'{self.project.title}', 'Python/Django site')
        self.assertEqual(f'{project_category.title}', 'Python')
        self.assertEqual(f'{project_team.get_name()}', 'Alex Argo')
        self.assertEqual(f'{self.project.short_description}', 'lalala')
#
#     def test_book_list_view(self):
#         response = self.client.get(reverse('book_list'))
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Harry Potter')
#         self.assertTemplateUsed(response, 'books/book_list.html')
#
#     def test_book_detail_view(self):
#         response = self.client.get(self.project.get_absolute_url())
#
#         no_response = self.client.get('/books/12345/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, 'Harry Potter')
#         self.assertContains(response, 'An excellent review')
#         self.assertTemplateUsed(response, 'books/book_detail.html')
#
#
# class ProjectCategoryTests(TestCase):
#     pass
#
#
# class ServiceTests(TestCase):
#     pass
#
#
# class ProfileTests(TestCase):
#     pass
#
#
# class NewsTests(TestCase):
#     pass
#
#
# class ContactTests(TestCase):
#     pass
#
#
#
#
#
#
#
# # ProjectsListView
# # CategoryProjectListView
# # ProjectDetailView
# # ServiceListView
# # ServiceDetailView
# # PeopleListView
# # CategoryProfileListView
# # ProfileView
# # NewsListView
# # NewsDetailView
# # ContactView
# # SuccessView
#
