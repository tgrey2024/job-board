from django.views.generic import ListView, DetailView
from .models import Employer, Applicant


class EmployerListView(ListView):
    model = Employer
    template_name = 'profiles/employer_list.html'
    context_object_name = 'employers'


class EmployerProfiles(DetailView):
    model = Employer
    template_name = 'profiles/employer_profile.html'
    context_object_name = 'employer'

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        return Employer.objects.get(employer__id=user_id)


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
        return Applicant.objects.get(applicant__id=user_id)