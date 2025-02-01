from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Employer(models.Model):
    company_name = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    logo = CloudinaryField('image', default='placeholder')
    site_url = models.URLField(blank=True)
    address1 = models.TextField(blank=True)
    address2 = models.TextField(blank=True)
    city = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.employer.username


class Applicant(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    intro = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    profilepic = CloudinaryField('image', default='placeholder')
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)
    skills = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.applicant.username