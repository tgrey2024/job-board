from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from profiles.models import Employer, Applicant
from django.views.generic.edit import CreateView
from .models import Job
from django.urls import reverse_lazy
from .models import Job, JobApplication
from .forms import JobApplicationForm


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

class JobApplicationCreateView(CreateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'jobboard/job_application_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = Job.objects.get(pk=self.kwargs['job_id'])
        return context

    def form_valid(self, form):
        form.instance.applicant = Applicant.objects.get(user=self.request.user)
        form.instance.job = Job.objects.get(pk=self.kwargs['job_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('job_detail', kwargs={'pk': self.kwargs['job_id']})
