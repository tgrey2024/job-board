from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from .models import Employer, Applicant


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
        return get_object_or_404(Applicant, applicant__id=user_id)