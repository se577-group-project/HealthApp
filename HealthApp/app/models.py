"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UsersProfile (models.Model):

    #connected to another database table that holds password and username
    username = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    #customertype determines the type of account is created
    #customertype False = Customer Profile
    #custoemrtype True = Business Profile
    customertype = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UsersProfile.objects.create(username=kwargs['instance'])

post_save.connect(create_profile, sender=User)
