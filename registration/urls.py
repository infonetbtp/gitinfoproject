from .import views
from django.urls import path
urlpatterns = [
    path('',views.SignUp, name='SignUp'),
    path('signIn/',views.signIn, name='signIn'),
    path('success/',views.success, name='success'),
    
    
]