from django.urls import path
from .views import EmployerListView, Profiles

urlpatterns = [
    path('employers/', EmployerListView.as_view(), name='employer_list'),
    path('<int:user_id>/', Profiles.as_view(), name='profile'),
]
