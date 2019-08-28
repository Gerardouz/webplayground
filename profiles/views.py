from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from registration.models import Profile 
# Create your views here.

class ProfileView(ListView):
    model = Profile


