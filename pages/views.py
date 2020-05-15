from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView

from .models import Project, Profile, News, Service, ProjectImage, ProjectCategory, ProfileCategory, group
from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


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
        pr = Project.objects.filter(project_category__category_slug=self.kwargs['category_slug'])
        return group(pr, 6)

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)

        data['category'] = self.get_category()
        return data

    def get_category(self):
        try:
            category = ProjectCategory.objects.get(category_slug=self.kwargs['category_slug'])
        except ProjectCategory.DoesNotExist:
            raise Http404
        return category


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'pages/project_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)

        data['images'] = self.get_images()
        return data

    def get_images(self):
        pr = ProjectImage.objects.filter(project__slug=self.kwargs['slug'])
        return group(pr, 4)


class ServiceListView(ListView):
    model = Service
    context_object_name = 'services_list'
    template_name = 'pages/service_list.html'
    paginate_by = 10


class ServiceDetailView(DetailView):
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


class CategoryProfileListView(PeopleListView):

    def get_queryset(self):
        pr = Profile.objects.filter(profile_category__category_slug=self.kwargs['category_slug'])
        return group(pr, 6)

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)

        data['category'] = self.get_category()
        return data

    def get_category(self):
        try:
            category = ProfileCategory.objects.get(category_slug=self.kwargs['category_slug'])
        except ProfileCategory.DoesNotExist:
            raise Http404
        return category


class ProfileView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'pages/profile.html'


class NewsListView(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'pages/news_list.html'
    paginate_by = 10


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'pages/news_detail.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'pages/contact.html'
    success_url = 'success/'

    def form_valid(self, form):
        self.send_email(form.cleaned_data)
        return super(ContactView, self).form_valid(form)

    def send_email(self, data):
        subject = data['subject']
        message = data['message']
        from_email = data['email']
        send_mail(subject, message, from_email, ['jekrudcz@gmail.com'])


class SuccessView(TemplateView):
    template_name = 'pages/success.html'
