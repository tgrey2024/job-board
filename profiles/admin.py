from django.contrib import admin
from .models import Applicant, Employer
from django_summernote.admin import SummernoteModelAdmin


# @admin.register(Employer)
# class EmployerAdmin(admin.ModelAdmin):

#     list_display = ('company_name', 'site_url', 'updated_on')
#     search_fields = ['company_name']
admin.site.register(Employer)

@admin.register(Applicant)
class ApplicantAdmin(SummernoteModelAdmin):
    list_display = ('firstname', 'lastname', 'role', 'updated_on')
    search_fields = ['firstname', 'lastname', 'role']
    summernote_fields = ('intro','skills','experience')

