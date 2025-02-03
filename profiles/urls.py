from django.urls import path
from .views import EmployerListView, Profiles, ApplicantListView
from .views import ApplicantProfile, ApplicantUpdateView

urlpatterns = [
    path('employers/', EmployerListView.as_view(), name='employer_list'),
    path('employer/<int:user_id>/', Profiles.as_view(), name='employer_profile'),
    path('applicants/', ApplicantListView.as_view(), name='applicant_list'),
    path('applicant/<int:user_id>/', ApplicantProfile.as_view(), name='applicant_profile'),
    path('profile/<int:user_id>/', ApplicantProfile.as_view(), name='profile'),
    # path('applicant/create/', ApplicantCreateView.as_view(), name='applicant_create'),
    path('applicant/update/<int:pk>/', ApplicantUpdateView.as_view(), name='applicant_update'),
]
