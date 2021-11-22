from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
User = get_user_model()

from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

# from . import forms
from authentication import models

# Create your views here.

class DoctorList(generic.ListView):
    model = models.Doctor
    template_name = 'Profile/doctor_list.html'


class NGOList(generic.ListView):
    model = models.NGO
    template_name = 'Profile/ngolist.html'


class DoctorDetail(generic.DetailView):
    model = models.Doctor
    template_name = 'Profile/doctorprofile.html'


class NGODetail(generic.DetailView):
    model = models.NGO
    template_name = 'Profile/ngoprofile.html'


