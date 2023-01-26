from django.urls import path

from solutions.views import HomePage, Project

app_name = 'solution'

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('projects/', Project.as_view(), name='projects'),

]
