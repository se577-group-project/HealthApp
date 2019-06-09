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
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('user_profile/<str:username>', views.get_user_profile, name='user_profile'),
    path('review/', views.review, name='review'),
    path('HealthCare/', views.ListSearchView.as_view(), name='search')
]
