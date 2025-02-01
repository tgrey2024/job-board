from django.contrib import admin
from .models import Applicant, Employer
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Employer)
class EmployerAdmin(SummernoteModelAdmin):

    list_display = ('company_name', 'content')
    search_fields = ['company_name']
    summernote_fields = ('content',)


@admin.register(Applicant)
class ApplicantAdmin(SummernoteModelAdmin):
    list_display = ('firstname', 'lastname', 'role', 'updated_on')
    search_fields = ['firstname', 'lastname', 'role']
    summernote_fields = ('intro','skills','experience')

