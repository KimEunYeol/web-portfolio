from django.urls import path

from .views import index, about, project


urlpatterns = [
    path('main/', index, name='main'),
    path('main/about', about, name='about'),
    path('main/project', project, name='project'),
]