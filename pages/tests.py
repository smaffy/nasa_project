
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .models import Project, ProjectCategory, Profile, Service
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


class ProjectAndProfileTests(TestCase):

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

        self.profile2 = Profile.objects.create(
            first_name='Lara',
            last_name='Mara',
            email='lama@email.com',
            short_description='kuku jamba'
        )

        self.project_category = ProjectCategory.objects.create(
            title='Python',
        )

        self.project_category2 = ProjectCategory.objects.create(
            title='JS',
        )

        self.project = Project.objects.create(
            title='Django site',
            short_description='lalala',
        )

        self.project2 = Project.objects.create(
            title='JS site',
            short_description='hehehe',
        )

        self.project.project_category.add(ProjectCategory.objects.get(title='Python'))
        self.project.project_team.add(Profile.objects.get(id=self.profile.id))

        self.project2.project_category.add(ProjectCategory.objects.get(title='JS'), ProjectCategory.objects.get(title='Python'))
        self.project2.project_team.add(Profile.objects.get(id=self.profile.id), Profile.objects.get(id=self.profile2.id))

        # self.review = Review.objects.create(
        #     book=self.book,
        #     author=self.user,
        #     review='An excellent review',
        # )

    def test_project_listing(self):
        project_team = self.project.project_team.first()
        project_category = self.project.project_category.first()

        self.assertEqual(f'{self.project.title}', 'Django site')
        self.assertEqual(f'{project_category.title}', 'Python')
        self.assertEqual(f'{project_team.get_name()}', 'Alex Argo')
        self.assertEqual(f'{self.project.short_description}', 'lalala')

    def test_project2_listing(self):
        project_team = self.project2.project_team.all()
        a = list(project_team).index(self.profile)
        b = list(project_team).index(self.profile2)
        project_category = self.project2.project_category.all()
        project_category.order_by('title')

        self.assertEqual(f'{self.project2.title}', 'JS site')
        self.assertEqual(f'{project_category[1].title}', 'Python')
        self.assertEqual(f'{project_category[0].title}', 'JS')
        self.assertEqual(f'{project_team[b].get_name()}', 'Lara Mara')
        self.assertEqual(f'{project_team[a].get_name()}', 'Alex Argo')
        self.assertEqual(f'{self.project2.short_description}', 'hehehe')

    def test_project_list_view(self):
        response = self.client.get(reverse('pages:projects'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django site')
        self.assertTemplateUsed(response, 'pages/projects_list.html')

    def test_category_project_list_view(self):
        response = self.client.get(reverse('pages:projects_category', kwargs={'category_slug': 'js'}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'JS site')
        self.assertNotContains(response, 'Django site')
        self.assertTemplateUsed(response, 'pages/projects_list.html')

    def test_category2_project_list_view(self):
        response = self.client.get(reverse('pages:projects_category', kwargs={'category_slug': 'python'}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'JS site')
        self.assertContains(response, 'Django site')
        self.assertTemplateUsed(response, 'pages/projects_list.html')

    def test_project_detail_view(self):
        response = self.client.get(self.project.get_absolute_url())
        no_response = self.client.get('/projects/12345/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Django site')
        self.assertContains(response, 'lalala')
        self.assertContains(response, 'Alex Argo')
        self.assertContains(response, 'Python')
        self.assertNotContains(response, 'Lara Mara')
        self.assertNotContains(response, 'hehehe')
        self.assertTemplateUsed(response, 'pages/project_detail.html')

    def test_project2_detail_view(self):
        response = self.client.get(self.project2.get_absolute_url())
        no_response = self.client.get('/projects/12345/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'JS site')
        self.assertContains(response, 'hehehe')
        self.assertContains(response, 'Lara Mara')
        self.assertContains(response, 'JS')
        self.assertContains(response, 'Alex Argo')
        self.assertContains(response, 'Python')
        self.assertTemplateUsed(response, 'pages/project_detail.html')


class ServiceTests(TestCase):

    def setUp(self):
        self.service = Service.objects.create(
            title='design',
            short_description='short_description',
            description='descriptiondescription descriptiondescription',
        )

    def test_service_listing(self):

        self.assertEqual(f'{self.service.title}', 'design')
        self.assertEqual(f'{self.service.short_description}', 'short_description')
        self.assertEqual(f'{self.service.description}', 'descriptiondescription descriptiondescription')

    def test_service_list_view(self):
        response = self.client.get(reverse('pages:service_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'short_description')
        self.assertNotContains(response, 'descriptiondescription descriptiondescription')
        self.assertTemplateUsed(response, 'pages/service_list.html')

    def test_service_detail_view(self):
        response = self.client.get(self.service.get_absolute_url())
        no_response = self.client.get('/service/12345/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'design')
        self.assertContains(response, 'short')
        self.assertContains(response, 'description')
        self.assertTemplateUsed(response, 'pages/service_detail.html')




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
