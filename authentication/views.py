import profile
from django.shortcuts import render, get_object_or_404, redirect 
from django.views import generic
from django.views.generic import  (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from . forms import UserForm, NormalProfileForm, NGOProfileForm, DoctorProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.http import HttpResponseRedirect,HttpResponse
from . models import User, Normal, NGO, Doctor
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q

# Create your views here.

def SignUp(request):
    return render(request, 'authentication/signup.html', {})


def NormalSignUp(request):
    user_type = 'normal'
    registered = False

    if request.method == "POST":
        print("Done")
        user_form = UserForm(request.POST, request.FILES)
        normal_profile_form = NormalProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and normal_profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_normal = True 
            user.save()

            profile = normal_profile_form.save(commit=False)
            profile.user = user 
            profile.save()

            registered = True 
            return HttpResponseRedirect(reverse('home'))

        else:
            print(user_form.errors, normal_profile_form.errors)
        
    else:
        user_form = UserForm()
        normal_profile_form = NormalProfileForm()

    return render(request, 'authentication/normal_signup.html', {'user_form':user_form, 'normal_profile_form': normal_profile_form, 'registered':registered, 'user_type':user_type})


def NGOSignUp(request):
    user_type = 'ngo'
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST)
        ngo_profile_form = NGOProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and ngo_profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_ngo = True 
            user.save()

            profile = ngo_profile_form.save(commit=False)
            profile.user = user 
            profile.save()

            registered = True 
            return HttpResponseRedirect(reverse('home'))

        else:
            print(user_form.errors, ngo_profile_form.errors)
        
    else:
        user_form = UserForm()
        ngo_profile_form = NGOProfileForm()

    return render(request, 'authentication/ngo_signup.html', {'user_form':user_form, 'ngo_profile_form': ngo_profile_form, 'registered':registered, 'user_type':user_type})


def DoctorSignUp(request):
    user_type = 'doctor'
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES)
        doctor_profile_form = DoctorProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and doctor_profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_doctor = True 
            user.save()

            profile = doctor_profile_form.save(commit=False)
            profile.user = user 
            profile.save()

            registered = True 
            return HttpResponseRedirect(reverse('home'))

        else:
            print(user_form.errors, doctor_profile_form.errors)
        
    else:
        user_form = UserForm()
        doctor_profile_form = DoctorProfileForm()

    return render(request, 'authentication/doctor_signup.html', {'user_form':user_form, 'doctor_profile_form': doctor_profile_form, 'registered':registered, 'user_type':user_type})

    
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("Account not active")

        else:
            messages.error(request, "Invalid Details")
            return redirect('authentication:login')
    else:
        return render(request,'authentication/login.html',{})


## logout view.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))






















    