"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator


class UsersProfile (models.Model):

    #connected to another database table that holds password and username
    username = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    #user profile bio is stored here
    bio = models.TextField(blank=True) 

    def __str__(self):
        return str(self.username)
    
#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = UsersProfile.objects.create(username=kwargs['instance'])

#post_save.connect(create_profile, sender=User)

class HealthCare (models.Model):
    
    #connected to another database table that holds password and username
    username = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    #business type
    #businesstype = models.TextField(default=False) 

    #user profile bio is stored here
    bio = models.TextField(blank=True) 

    #business website if users want to visit
    website = models.URLField(max_length=50, blank=True)

    #business contact number
    phonenumber = models.CharField(max_length=20, blank=True)

    #location of business
    location = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.username)


class Reviews (models.Model):
    
    #each review is associated with a company and a profile
    business = models.ForeignKey(HealthCare, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(UsersProfile, on_delete=models.CASCADE)

    #review of a store
    review = models.TextField(default=False)
    
    #store stars as integer 1 - 5 for thge amount of stars
    stars = models.IntegerField(default=1,
                                validators=[MaxValueValidator(5), MinValueValidator(1)]
                                )

