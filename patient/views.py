from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient




@login_required(login_url="/login/")
def get_one_patient(request,patient_id):
    patient = get_object_or_404(Patient,id = patient_id )
    return render(request, 'patient/patient_detail.html', {'patient': patient})
