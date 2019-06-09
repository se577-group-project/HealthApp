"""
Definition of views.
"""
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth import login as auth_login, logout, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from app.database_interface import Database_Interface
from app.user_verification import User_Verification



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def login(request):
    if request.method == 'POST':
        if request.POST.get('loginbtn'):
            username = request.POST.get('usernameLogin')
            password = request.POST.get('passwordLogin')

            if User_Verification.login_verify(request, username, password): 
                user = authenticate(username=username, password=password)
                if user:
                    if user.is_active:
                        auth_login(request,user)
                        return HttpResponseRedirect(reverse('home'))
                messages.error(request,'There was an error when you tried to login.. please try again', extra_tags='SignUpError')
        elif request.POST.get('signupbtn'):
            username = request.POST.get('usernameSignup')
            email = request.POST.get('emailSignupPri')
            password = request.POST.get('passwordSignupPri')
            passwordVerifiction = request.POST.get('passwordSignupSec')

            if User_Verification.signup_verify(request, username, email, password, passwordVerifiction): 

                #figure out what type of customer signed up and what database they belong too 
                if request.POST.get('optradio') == 'Customer':
                    UserCheck = Database_Interface.set_userprofile(request,email,username,password,'')
                else: 
                    UserCheck = Database_Interface.set_healthcare(request, email, username, password, '', '', '','')
                
                if UserCheck:
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        auth_login(request,user)
                        return HttpResponseRedirect(reverse('home'))
                else:
                    messages.error(request,'A username or email already exists', extra_tags='SignUpError')
        return render(request, 'app/login.html')
     
    else:
        return render(request, 'app/login.html', {})




def search(request): 
    """Renders the search page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/search.html',
        {
            'title':'Search',
            'message':'Your search page.',
            'year':datetime.now().year,
        }
    )

def profile(request): 
    """Renders the profile page."""
    assert isinstance(request, HttpRequest)
    profile_type = Database_Interface.check_profile_type(request.user.id)
    if profile_type.lower() == "business":
        profile_data = Database_Interface.get_healthcare(request.user.id)
        reviews = Database_Interface.get_reviews_by_healthcare(request.user.id)
    else:
        profile_data = Database_Interface.get_userprofile(request.user.id)
        reviews = Database_Interface.get_reviews_by_user(request.user.id)
    return render(
        request,
        'app/profile.html',
        {"profile_type": profile_type,
         "profile_data": profile_data,
         "reviews": reviews}
    )


def get_user_profile(request, username):
    _user = User.objects.get(username=username)
    profile_type = Database_Interface.check_profile_type(_user.id)
    if profile_type.lower() == "business":
        profile_data = Database_Interface.get_healthcare(_user.id)
        reviews = Database_Interface.get_reviews_by_healthcare(_user.id)
    else:
        profile_data = Database_Interface.get_userprofile(_user.id)
        reviews = Database_Interface.get_reviews_by_user(_user.id)

    return render(request, 'app/user_profile.html', 
                  {"profile_user": _user,
                   "profile_type": profile_type,
                   "profile_data": profile_data,
                   "reviews": reviews})