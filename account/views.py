from django.shortcuts import render, redirect
from account.forms import StaffRegistrationForm,DoctorRegistrationForm  # and DoctorRegistrationForm if you have it

def register_view(request):
    if request.method == 'POST':
        submit_type = request.POST.get('submit_type')

        if submit_type == 'staff':
            staff_form = StaffRegistrationForm(request.POST)
            doctor_form = DoctorRegistrationForm()  # empty for display
            if staff_form.is_valid():
                staff_form.save()
                return redirect('staff_dashboard')  # or a success page
        elif submit_type == 'doctor':
            doctor_form = DoctorRegistrationForm(request.POST)
            staff_form = StaffRegistrationForm()
            if doctor_form.is_valid():
                doctor_form.save()
                return redirect('staff_dashboard')
    else:
        staff_form = StaffRegistrationForm()
        doctor_form = DoctorRegistrationForm()

    return render(request, 'account/register.html', {
        'staff_form': staff_form,
        'doctor_form': doctor_form,
    })
