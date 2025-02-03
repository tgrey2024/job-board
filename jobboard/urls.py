from django.urls import path
from .views import HomePage, JobDetailView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
]
