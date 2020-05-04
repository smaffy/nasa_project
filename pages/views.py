from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Project, Profile, News, Service, ProjectImage


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class ProjectsListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'pages/projects_list.html'
    paginate_by = 10

    def get_images(self):
        return ProjectImage.objects.filter(project__slug=self.kwargs['slug'])


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'pages/project_detail.html'


class ServicesView(ListView):
    model = Service
    context_object_name = 'services_list'
    template_name = 'pages/services.html'
    paginate_by = 10


class PeopleListView(ListView):
    model = Profile
    context_object_name = 'people_list'
    template_name = 'pages/people_list.html'
    paginate_by = 10


class ProfileView(DetailView):
    model =  Profile
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


class ContactView(TemplateView):
    template_name = 'pages/contact.html'

