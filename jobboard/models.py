from django.db import models
from django.contrib.auth.models import User
from profiles.models import Employer, Applicant

# Status choices for Application model
STATUS = (
    (0, "Pending"),
    (1, "Interviewed"),
    (2, "Rejected"),
    (3, "Hired")
)

class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name="job_listings")
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class JobApplication(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name="applications")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    cover_letter = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        unique_together = ('applicant', 'job')

    def __str__(self):
        return f"{self.applicant} - {self.job}"