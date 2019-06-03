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

    #user profile bio is stored here
    bio = models.TextField(default=False) 

    def __str__(self):
        return str(self.username)
    
#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = UsersProfile.objects.create(username=kwargs['instance'])

#post_save.connect(create_profile, sender=User)

class HealthCare (models.Model):
    
    #connected to another database table that holds password and username
    username = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    #user profile bio is stored here
    bio = models.TextField(default=False) 

    #business website if users want to visit
    website = models.CharField(max_length=50)

    #business contact number
    phonenumber = models.CharField(max_length=20, blank=True)

    #location of business
    location = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.username)


#class Reviews (models.Model):
    
    #each review is assiated with a company
#    hc_id = models.ForeignKey(HealthCare, on_delete=models.CASCADE)
    
#    user_id = models.CharField(max_length=20, blank=True)

    #review of a store
#    review = models.TextField(default=False)

    #store an dup incase user has mutiple reviews for the same company
#    dup = models.CharField(max_length=1, blank=True)
    
    #store stars as text 1 - 5 for thge amount of stars
#    stars = models.CharField(max_length=1, blank=True)

