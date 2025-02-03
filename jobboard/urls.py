from django.urls import path
from .views import HomePage, JobDetailView, JobApplicationCreateView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('job/<int:job_id>/apply/', JobApplicationCreateView.as_view(), name='job_apply'),
]
