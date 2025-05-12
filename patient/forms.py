from django import forms
from .models import Patient


class PatientForm(forms.Form):
    first_name = forms.CharField(min_length=2, required=True)
    last_name = forms.CharField(min_length=2, required=True)
    phone = forms.CharField(min_length=10, required=True)
    gender = forms.CharField(min_length=4, max_length=6)
    email = forms.EmailField()
    address = forms.CharField()
