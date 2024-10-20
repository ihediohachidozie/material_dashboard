# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.home.urls")),             # UI Kits Html files
    path('accounts/register/', RegistrationView.as_view(success_url='/'), name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('accounts/', include('django.contrib.auth.urls')), # Auth routes
    #path("", include("apps.authentication.urls")), # Auth routes - login / register
]
