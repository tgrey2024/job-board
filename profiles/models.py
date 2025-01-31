from django.db import models
from django.contrib.auth.models import User


class EmployerProfile(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ApplicantProfile(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title