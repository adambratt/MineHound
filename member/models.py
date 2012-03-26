from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Member(models.Model):
    user = models.OneToOneField(User)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)