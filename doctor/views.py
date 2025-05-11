from django.shortcuts import render









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
    return render(request, "doctor/doctor_appointments.html")



def list_assigned_patients(request):
    return render(request, "doctor/doctor_patients.html")


