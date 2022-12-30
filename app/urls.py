from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='abt'),
    path('booking', views.booking,name='book'),
    path('doctors', views.doctors,name='doc'),
    path('contact', views.contact,name='cont'),
    path('department', views.department,name='dept'), 
   
]
                                                                              