from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView
from parler.views import TranslatableSlugMixin, ViewUrlMixin

from users.models import CustomUser
from .models import Project, Profile, News, Service, ProjectImage, ProjectCategory, ProfileCategory, group
from .forms import ContactForm


class ElementsView(TemplateView):
    template_name = 'pages/elements.html'


class IconsView(TemplateView):
    template_name = 'pages/elements_icons.html'


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)

        data['hprojects'] = self.get_projects()
        data['hservices'] = self.get_services()
        data['hnews'] = self.get_news()
        data['hteam'] = self.get_team()
        return data

    def get_projects(self):
        return Project.objects.all()[:4]

    def get_services(self):
        serv = Service.objects.all()[:6]
        return group(serv, 3)

    def get_news(self):
        return News.objects.all()[:6]

    def get_team(self):
        return Profile.objects.all()[:8]


class ProjectsListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'pages/projects_list.html'
    paginate_by = 1

    def get_queryset(self):
        pr = Project.objects.all()
        return group(pr, 6)


class CategoryProjectListView(ProjectsListView):

    def get_queryset(self):
        categ = ProjectCategory.objects.get(translations__category_slug=self.kwargs['category_slug'])
        pr = Project.objects.filter(project_category=categ)
        # pr = Project.objects.filter(project_category__category_slug=self.kwargs['category_slug'])
        return group(pr, 6)

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)

        data['category'] = self.get_category()
        return data

    def get_category(self):
        try:
            category = ProjectCategory.objects.get(translations__category_slug=self.kwargs['category_slug'])
            # category = ProjectCategory.objects.get(category_slug=self.kwargs['category_slug'])
        except ProjectCategory.DoesNotExist:
            raise Http404
        return category


class ProjectDetailView(TranslatableSlugMixin, DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'pages/project_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)

        imag = self.object.get_images()
        data['images'] = imag

        return data

    # def get_project(self):
    #     # pr = ProjectImage.objects.filter(project__slug=self.kwargs['slug'])
    #     return Project.objects.get(slug=self.get_object())

    def get_images(self):
        project = Project.objects.language('en').get(translations__slug=self.object.slug)
        img = ProjectImage.objects.filter(project__id=project.id)
        return group(img, 4)


class ServiceListView(ListView):
    model = Service
    context_object_name = 'allservices'
    template_name = 'pages/service_list.html'
    paginate_by = 10


class ServiceDetailView(TranslatableSlugMixin, DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'pages/service_detail.html'


class PeopleListView(ListView):
    model = Profile
    context_object_name = 'people_list'
    template_name = 'pages/people_list.html'
    paginate_by = 3

    def get_queryset(self):
        pr = Profile.objects.all()
        return group(pr, 3)


class CategoryProfileListView(ViewUrlMixin, PeopleListView):
    view_url_name = 'pages:profile_category'

    def get_queryset(self):
        # pr = Profile.objects.filter(profile_category__category_slug=self.kwargs['category_slug'])
        categ = ProfileCategory.objects.get(translations__category_slug=self.kwargs['category_slug'])
        pr = Profile.objects.filter(profile_category=categ)

        return group(pr, 6)

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)

        data['category'] = self.get_category()
        return data

    def get_category(self):
        try:
            # category = ProfileCategory.objects.get(category_slug=self.kwargs['category_slug'])
            category = ProfileCategory.objects.get(translations__category_slug=self.kwargs['category_slug'])
        except ProfileCategory.DoesNotExist:
            raise Http404
        return category


class ProfileView(TranslatableSlugMixin, DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'pages/profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)

        data['projects'] = self.get_projects()

        return data

    def get_projects(self):
        profile = Profile.objects.get(translations__slug=self.object.slug)
        pr = profile.projects.all()
        return group(pr, 4)


class NewsListView(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'pages/news_list.html'
    paginate_by = 10


class NewsDetailView(TranslatableSlugMixin, DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'pages/news_detail.html'


class AboutView(HomePageView):
    template_name = 'pages/about.html'


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'pages/contact.html'
    success_url = 'success/'

    def form_valid(self, form):
        self.send_email(form.cleaned_data)
        return super(ContactView, self).form_valid(form)

    def send_email(self, data):
        subject = data['name'] + ' ' + data['subject']
        message = data['message']
        from_email = data['email']
        if CustomUser.objects.get(username='company').email:
            contacts = CustomUser.objects.get(username='company')
            send_mail(subject, message, from_email, [contacts.email, ])
        else:
            send_mail(subject, message, from_email, ['rudakovacz@gmail.com', ])
        

class SuccessView(TemplateView):
    template_name = 'pages/success.html'
