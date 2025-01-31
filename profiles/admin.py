from django.contrib import admin
from .models import ApplicantProfile, EmployerProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ApplicantProfile)
class ApplicantProfileAdmin(SummernoteModelAdmin):
    list_display = ('title', 'content')
    search_fields = ['title']
    summernote_fields = ('content',)


@admin.register(EmployerProfile)
class EmployerProfileAdmin(SummernoteModelAdmin):

    list_display = ('title', 'content')
    search_fields = ['title']
    summernote_fields = ('content',)
