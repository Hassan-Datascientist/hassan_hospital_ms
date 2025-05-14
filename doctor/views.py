from django.shortcuts import render
from appointment.models import Appointment
from doctor.models import Doctor
from patient.models import Patient






def doctor_dash(request):
    return render(request, "doctor/doctor_dashboard.html")


def doctor_profile(request, id):
    form = ""
    if request.method == "POST":
        form = ""
        if form.is_valid():
            pass

    return render(request, "doctor/doctor_profile.html", {"form": form})



def list_appointments(request):
    appointments = Appointment.objects.filter(doctor__user=request.user)
    print(appointments)

    context = {
        "appointments": appointments
    }

    return render(request, "doctor/doctor_appointments.html", context)



def list_assigned_patients(request):
    doctor = Doctor.objects.get(user=request.user)
    patients = Patient.objects.filter(appointment__doctor=doctor).distinct()
    context = {
        "patients": patients
    }
    return render(request, "doctor/doctor_patients.html", context)


