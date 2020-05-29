from django.urls import path, include
from django.utils.translation import gettext_lazy as _
# _(''),

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path(_('about_us/'), views.AboutView.as_view(), name='about'),

    path(_('projects/'), views.ProjectsListView.as_view(), name='projects'),
    path(_('projects/category') + '/<slug:category_slug>/', views.CategoryProjectListView.as_view(), name='projects_category'),
    path(_('projects') + '/<slug:slug>/', views.ProjectDetailView.as_view(), name='projects_detail'),
    path(_('service/'), views.ServiceListView.as_view(), name='service_list'),
    path(_('service') + '/<slug:slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path(_('people/'), views.PeopleListView.as_view(), name='people'),
    path(_('people/category') + '/<slug:category_slug>/', views.CategoryProfileListView.as_view(), name='profile_category'),
    path(_('people') + '/<slug:slug>/', views.ProfileView.as_view(), name='profile'),
    path(_('news/'), views.NewsListView.as_view(), name='news'),
    path(_('news') + '/<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail'),
    path(_('contact/'), views.ContactView.as_view(), name='contact'),
    path(_('contact/success/'), views.SuccessView.as_view(), name='success'),

]
