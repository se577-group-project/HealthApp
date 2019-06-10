'''
database_interface is an interface for model.py (database) 
this file is to be used for all database access
if functionailty does not exist, update this model and not the database itself
'''

from django.contrib.auth.models import User
from app.models import UsersProfile, HealthCare, Reviews
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
    def update_userprofile (username, bio):
        _obj = UsersProfile.objects.get(pk=username)
        _obj.bio = bio
        _obj.save()
        return True

    @staticmethod
    def update_healthcare (username, bio, location, website, phonenumber):
        _obj = HealthCare.objects.get(pk=username)
        _obj.bio = bio
        _obj.location = location
        _obj.website = website
        _obj.phonenumber = phonenumber
        _obj.save()
        return True


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

    @staticmethod
    def get_all_healthcare():
        return HealthCare.objects.all()

    @staticmethod
    def get_reviews_by_healthcare (id):
        return list(Reviews.objects.filter(business_id=id).values('stars', 'review', 'reviewer__username__username'))

    @staticmethod
    def get_reviews_by_user (id):
        return list(Reviews.objects.filter(reviewer_id=id).values('stars', 'review', 'business__username__username'))


    @staticmethod
    def set_review (request, CustomerUsername, BusinessUsername, review, stars):
        cid = User.objects.get(username=CustomerUsername).id
        bid = User.objects.get(username=BusinessUsername).id
        _review = Reviews(reviewer_id=cid, business_id=bid, review=review, stars=stars)
        _review.save()
        return True

    @staticmethod
    def search_healthcare(username):
        return HealthCare.objects.filter(username__username__icontains=username)

    @staticmethod
    def delete_account(request):
        request.user.delete()
        logout(request)
        return True

    @staticmethod
    def delete_comment(request):
        insance = Reviews.objects.filter(id=request.user.id)
        insance.delete()
        return True

        #TODO complete function
    @staticmethod
    def update_profile (username, email, password):
        return True

