from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Project, Profile, News, Service, ProjectImage


def group(iterable, count):
    return list(zip(*[iter(iterable)] * count))


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class ProjectsListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'pages/projects_list.html'
    paginate_by = 1

    def get_images(self):
        return ProjectImage.objects.filter(project__slug=self.kwargs['slug'])

    def get_queryset(self):
        pr = Project.objects.all()
        return group(pr, 4)

        # pr = Project.objects.all()[::2]
        # pr2 = Project.objects.all()[1::2]
        # if len(pr) == len(pr2):
        #     projects1 = [[i, m] for i in pr for m in pr2]
        # else:
        #     projects1 = [[i, m] for i in pr[:-1] for m in pr2]
        # return projects1

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)

        data['projects'] = self.get_queryset()
        return data


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'pages/project_detail.html'


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
    paginate_by = 10


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


class ContactView(TemplateView):
    template_name = 'pages/contact.html'

