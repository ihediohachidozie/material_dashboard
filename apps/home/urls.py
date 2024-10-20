# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path("profile-saved/", views.saveProfile, name="saveProfile")

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

]
