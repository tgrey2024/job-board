from django.views.generic import ListView, DetailView
from .models import Employer


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
        return Employer.objects.get(employer__id=user_id)