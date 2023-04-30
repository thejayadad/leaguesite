from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse


from django.views import generic 

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')