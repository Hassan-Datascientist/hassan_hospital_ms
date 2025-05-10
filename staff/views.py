from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from patient.models import Patient
from patient.forms import PatientForm
from django.contrib.auth.decorators import login_required

@login_required(login_url = "/login/")
def staff_dashboard(request):
    return render(request, 'staff/staff_dashboard.html')

@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_dashboard')
    else:
        form = PatientForm()
    return render(request, 'patient/add_patient.html', {'form': form})

@login_required
def get_all_patient(request):
    patients = Patient.objects.all()
    return render(request, 'patient/list_patient.html',{'patients':patients})

@login_required
def get_one_patient(request,patient_id):
    patient = get_object_or_404(Patient,id = patient_id )
    return render(request, 'patient/patient_detail.html', {'patient': patient})







# Getting all stuff members, path: /staff/
def get_staffs(request):
    #
    return render(request, 'staff/staff_list.html')


# path: /staff/id/
def get_staff(request, id):
    return render(request, "staff/staff_info.html")


# path: /staff/id/
def delete_staff(request, id):
    return HttpResponse(f"Deleting a member with an {id}")



# path: /staff/id/
def update_staff(request, id):
    return HttpResponse(f"Updating a member with {id}")
