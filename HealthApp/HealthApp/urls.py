"""
Definition of urls for HealthApp.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
