from django import forms
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
  first_name = forms.CharField()
  last_name = forms.CharField()

  class Meta:
    model = User
    fields = ['first_name', 'last_name'] 