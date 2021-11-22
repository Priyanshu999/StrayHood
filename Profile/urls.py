from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('doctors/', views.DoctorList.as_view(), name='alldoctors'),
    path('ngos/', views.NGOList.as_view(), name='allngo'),
    path('by/<username>/<int:pk>', views.DoctorDetail.as_view(), name='singledoctor'),
    path('byy/<username>/<int:pk>', views.NGODetail.as_view(), name='singlengo'),
]
