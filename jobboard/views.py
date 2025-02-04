from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from profiles.models import Employer, Applicant
from django.views.generic.edit import CreateView
from .models import Job
from django.urls import reverse_lazy
from .models import Job, JobApplication
from .forms import JobApplicationForm
from django.core.paginator import Paginator


class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'jobboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employers'] = Employer.objects.all()
        context['applicants'] = Applicant.objects.all()
        job_list = Job.objects.all()
        paginator = Paginator(job_list, 6)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        context['jobs'] = page_obj.object_list
        context['is_paginated'] = page_obj.has_other_pages()
        return context


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobboard/job_detail.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['has_applied'] = JobApplication.objects.filter(applicant__user=self.request.user, job=self.object).exists()
        else:
            context['has_applied'] = False
        return context

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
