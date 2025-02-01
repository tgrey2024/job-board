from django.shortcuts import render
from django.views.generic import TemplateView
from profiles.models import Employer


class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'jobboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employers'] = Employer.objects.all()
        return context
