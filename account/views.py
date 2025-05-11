from django.shortcuts import render, redirect
from account.forms import StaffRegistrationForm,DoctorRegistrationForm  # and DoctorRegistrationForm if you have it
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required



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





def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email, password = cd['email'], cd['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_doctor:
                    # redirect to doctor page
                    return redirect("/")

                # redirect to staff page
                return redirect("staff_dashboard")


            else:
                form.add_error(None, "Incorrect email or password")
                context = {"form": form}
                print(dir(form))
                print("Not Authenticated")
                # return render(request, "account/login.html", context)
    context = {"form": form}
    return render(request, "account/login.html", context)

@login_required
def logout_user(request):
    logout(request)
    return redirect("/")



def home(request):
    return render(request, "home.html")