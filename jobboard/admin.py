from django.contrib import admin
from .models import Job, JobApplication
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):
    list_display = ('title', 'employer', 'location', 'salary', 'created_on')
    search_fields = ['title', 'employer__company_name']
    summernote_fields = ('description',)

@admin.register(JobApplication)
class JobApplicationAdmin(SummernoteModelAdmin):
    list_display = ('applicant', 'job', 'created_on')
    search_fields = ['applicant__firstname', 'job__title']
    summernote_fields = ('cover_letter',)
