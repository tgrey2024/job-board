from .models import Applicant
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_profiles(sender, instance, created, **kwargs):
    if created:
        Applicant.objects.create(
            user=instance,
            firstname=instance.username,
            lastname="",
            role="",
            intro="",
            address1="",
            address2="",
            city="",
            postcode="",
            skills="",
            experience="",
        )