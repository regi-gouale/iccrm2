from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'common/login.html'
