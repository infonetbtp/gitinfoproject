from .import views
from django.urls import path
urlpatterns = [
    path('',views.deskboard, name='deskboard'),
    path('stu_logout/',views.stu_logout, name='stu_logout'),
    path('stu_profile_edit/',views.stu_profile_edit, name='stu_profile_edit'),
    
    
]