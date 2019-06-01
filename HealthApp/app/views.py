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
from app.models import UsersProfile
from django.contrib.auth.models import User


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

            #verify(username, password) TODO: uncomment when method is implemented

            user = authenticate(username=username, password=password)
            
            if user:
                if user.is_active:
                    auth_login(request,user)
                    return HttpResponseRedirect(reverse('home'))
        
        if request.POST.get('signupbtn'):
            username = request.POST.get('usernameSignup')
            password = request.POST.get('passwordSignupPri')
            passwordVerifiction = request.POST.get('passwordSignupSec')

            if True:#verify(username, password):

                user = User.objects.create_user(username=username, email='JohnDoe@beatles.com', password=password)
                user.save()

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    auth_login(request,user)
            
                    return HttpResponseRedirect(reverse('home'))
        
        message = {'Error' : 'There was an error when you tried to login.. please try again',}
        context = {'message' : message}

        return render(request, 'app/login.html', {'context': context})
     
    else:
        return render(request, 'app/login.html', {})

        #TODO create a verification function
        def verify(username, password):
            return True




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
