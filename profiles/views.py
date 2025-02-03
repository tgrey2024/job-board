from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Employer, Applicant
from .forms import ApplicantForm


class EmployerListView(ListView):
    model = Employer
    template_name = 'profiles/employer_list.html'
    context_object_name = 'employers'


class Profiles(DetailView):
    model = Employer
    template_name = 'profiles/employer_profile.html'
    context_object_name = 'employer'

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        try:
            return Employer.objects.get(employer__id=user_id)
        except Employer.DoesNotExist:
            return redirect('applicant_profile', user_id=user_id)


class ApplicantListView(ListView):
    model = Applicant
    template_name = 'profiles/applicant_list.html'
    context_object_name = 'applicants'


class ApplicantProfile(DetailView):
    model = Applicant
    template_name = 'profiles/applicant_profile.html'
    context_object_name = 'applicant'

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        return Applicant.objects.get(user__id=user_id)


class ApplicantCreateView(CreateView):
    model = Applicant
    form_class = ApplicantForm
    template_name = 'profiles/applicant_form.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        return context

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'user_id': self.object.user.id})


class ApplicantUpdateView(UpdateView):
    model = Applicant
    form_class = ApplicantForm
    template_name = 'profiles/applicant_form.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'user_id': self.object.user.id})
