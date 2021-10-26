from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_normal = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_ngo = models.BooleanField(default=False)


class Normal(models.Model):
    SEX_FEMALE = 'F'
    SEX_MALE = 'M'
    SEX_UNSURE = 'U'

    SEX_OPTIONS = (
        (SEX_FEMALE, 'Female'),
        (SEX_MALE, 'Male'),
        (SEX_UNSURE, 'Unsure')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="normals")
    name = models.CharField(max_length=254)
    age = models.IntegerField(blank=True, null=True)
    contact = models.IntegerField(blank=True)
    sex = models.CharField(max_length=1, choices=SEX_OPTIONS)
    address=models.CharField(max_length=250, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="users/normal_profile_pic", blank=True)

    def __str__(self):
        return "@{}".format(self.user.username)


class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="ngos")
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100, unique=True)
    contact = models.IntegerField(blank=True)
    profile_pic = models.ImageField(upload_to="users/ngo_profile_pic", blank=True)

    def __str__(self):
        return "@{}".format(self.user.username)
        

class Doctor(models.Model):
    SEX_FEMALE = 'F'
    SEX_MALE = 'M'
    SEX_UNSURE = 'U'

    SEX_OPTIONS = (
        (SEX_FEMALE, 'Female'),
        (SEX_MALE, 'Male'),
        (SEX_UNSURE, 'Unsure')
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctors")
    name = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    contact = models.IntegerField(blank=True)
    address = models.CharField(max_length=100, unique=True)
    age = models.IntegerField(blank=True, null=True)
    qualification = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=SEX_OPTIONS)
    profile_pic = models.ImageField(upload_to="users/doctor_profile_pic", blank=True)

    def __str__(self):
        return "@{}".format(self.user.username)
