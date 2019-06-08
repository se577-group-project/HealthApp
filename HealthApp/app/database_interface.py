'''
database_interface is an interface for model.py (database) 
this file is to be used for all database access
if functionailty does not exist, update this model and not the database itself
'''

from django.contrib.auth.models import User
from app.models import UsersProfile, HealthCare
from django.shortcuts import get_object_or_404, render
#from app.models import Reviews

class Database_Interface ():
    
    def __init__(self):
        super(Database_Interface, self).__init__()

    @staticmethod
    def set_profile (username, email, password):
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return user
   
    @staticmethod
    def set_userprofile (request, email, username, password, bio):
        if Database_Interface.check_profile (username, email):
            users = Database_Interface.set_profile (username, email, password)
            UsersProfile(username=users,bio=bio).save()
            return True
        return False

    @staticmethod
    def set_healthcare (request, email, username, password, bio, location, website, phonenumber):
        if Database_Interface.check_profile (username, email):
            users = Database_Interface.set_profile (username,email,password)
            HealthCare(username=users, bio=bio,website=website,phonenumber=phonenumber,location=location).save()
            return True
        return False


    @staticmethod
    def check_profile (username, email):
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists() :
            return False
        return True

    @staticmethod
    def check_profile_type(id):
        return "Business" if HealthCare.objects.filter(pk=id).exists() else "Customer"

    @staticmethod
    def get_userprofile (id):
        obj = get_object_or_404(UsersProfile, pk=id)
        return obj.__dict__

    @staticmethod
    def get_healthcare (id):
        obj = get_object_or_404(HealthCare,pk=id) 
        return obj.__dict__


    #TODO complete function
    @staticmethod
    def set_review (request, CustomerUsername, BusinessUsername, review, stars):
        return True


    #TODO complete function
    @staticmethod
    def get_review (BusinessUsername):
        return True

    #TODO complete function
    @staticmethod
    def update_profile (username, email, password):
        return True

    #TODO complete function
    @staticmethod
    def update_userprofile (username, password, bio):
        return True

    #TODO complete function
    @staticmethod
    def update_healthcare (username, password, bio, address, website, phonenumber,location):
        return True

    #TODO complete function
    @staticmethod
    def delete_account(username):
        return True

    #TODO complete function
    @staticmethod
    def delete_comment(BusinessUsername, CustomerUsername, ID):
        return True

