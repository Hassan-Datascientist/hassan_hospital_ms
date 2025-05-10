from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login






def register(request):
    return render(request, "account/register.html")



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
                    return redirect("staff-list")

                # redirect to staff page
                return redirect("staff-list")


            else:
                form.add_error(None, "Incorrect email or password")
                context = {"form": form}
                print(dir(form))
                print("Not Authenticated")
                # return render(request, "account/login.html", context)
    context = {"form": form}
    return render(request, "account/login.html", context)