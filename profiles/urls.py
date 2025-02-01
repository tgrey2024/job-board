from django.urls import path
from .views import EmployerListView, Profiles, ApplicantListView
from .views import ApplicantProfile

urlpatterns = [
    path('employers/', EmployerListView.as_view(), name='employer_list'),
    path('<int:user_id>/', Profiles.as_view(), name='profile'),
    path('applicants/', ApplicantListView.as_view(), name='applicant_list'),
    path('applicant/<int:user_id>/', ApplicantProfile.as_view(),
         name='applicant_profile'),

]
