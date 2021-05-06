from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optionel')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optionel')
    email = forms.CharField(max_length=255, required=False, help_text='Insérer une adresse mail valide')

    class Meta(object):
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]