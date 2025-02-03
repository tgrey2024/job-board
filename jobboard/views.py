from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from profiles.models import Employer, Applicant
from .models import Job

class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'jobboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employers'] = Employer.objects.all()
        context['applicants'] = Applicant.objects.all()
        context['jobs'] = Job.objects.all()
        return context


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobboard/job_detail.html'
    context_object_name = 'job'
