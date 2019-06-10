"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import HealthCare, UsersProfile

#TODO: Remove
class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class EditHealthCareProfileForm(UserChangeForm):
    
    class Meta:
        model = HealthCare
        fields = ['bio', 'website', 'phonenumber', 'location', 'password']

class EditUsersProfileForm(UserChangeForm):
    
    class Meta:
        model = UsersProfile
        fields = ['bio', 'password']