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
        if request.POST.get('signupbtn'):
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




def contact(request): ##TODO: Remove Module
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request): ##TODO: Remove module
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
