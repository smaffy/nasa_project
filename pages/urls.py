from django.urls import path, include
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('projects/', views.ProjectsListView.as_view(), name='projects'),
    path('projects/category/<slug:category_slug>/', views.CategoryProjectListView.as_view(), name='category'),
    path('projects/<slug:slug>/', views.ProjectDetailView.as_view(), name='projects_detail'),
    path('service/', views.ServiceListView.as_view(), name='service_list'),
    path('service/<slug:slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('people/', views.PeopleListView.as_view(), name='people'),
    path('people/<slug:slug>/', views.ProfileView.as_view(), name='profile'),
    path('news/', views.NewsListView.as_view(), name='news'),
    path('news/<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('about_us/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/success/', views.SuccessView.as_view(), name='success'),

]
