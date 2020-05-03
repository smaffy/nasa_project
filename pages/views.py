from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView


class HomePageView(TemplateView):
    template_name = '_base.html'


class ProjectsListView(ListView):
    template_name = 'pages/projects_list.html'


class ProjectDetailView(DetailView):
    template_name = 'pages/project_detail.html'


class ServicesView(ListView):
    template_name = 'pages/services.html'


class PeopleListView(ListView):
    template_name = 'pages/people_list.html'


class ProfileView(DetailView):
    template_name = 'pages/profile.html'


class NewsListView(ListView):
    template_name = 'pages/news_list.html'


class NewsDetailView(DetailView):
    template_name = 'pages/news_detail.html'


class ContactView(TemplateView):
    template_name = 'pages/contact.html'

