from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from patient.models import Patient
from patient.forms import PatientForm
from django.contrib.auth.decorators import login_required
from .forms import StaffUpdateForm
from account.models import User
from patient.models import Patient

@login_required(login_url = "/login/")
def staff_dashboard(request):
    return render(request, 'staff/staff_dashboard.html')

@login_required(login_url="/login/")
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            date = request.POST.get("date")
            patient = Patient(**cleaned_data)
            patient.created_by = request.user
            patient.date_of_birth = date
            patient.save()

            return redirect('staff_dashboard')
    else:
        form = PatientForm()
    return render(request, 'patient/add_patient.html', {'form': form})

@login_required(login_url="/login/")
def get_all_patient(request):
    patients = Patient.objects.all()
    return render(request, 'patient/list_patient.html',{'patients':patients})




@login_required(login_url="/login/")
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
    try:
        user = User.objects.get(id=id)

    except Exception as e:
        user = None

    if user is not None:
        form = StaffUpdateForm(request.POST, instance=user)
        if request.method == "POST":
            form = StaffUpdateForm(request.POST, instance=user)
            if form.is_valid():
                form.save()

        context = {"form": form}

        return render(request, "staff/update_staff.html", context)


def test(request):
    return render(request, "staff/test.html")
