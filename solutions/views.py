from django.views.generic import TemplateView, ListView

from solutions.models import Solution


class HomePage(TemplateView):
    template_name = 'solutions/homepage.html'


class Project(ListView):
    model = Solution
    template_name = 'solutions/projects.html'
