from django.urls import path
from .views import doctor_dash, doctor_profile, list_appointments, list_assigned_patients





urlpatterns = [
    path("dashboard/", doctor_dash, name="doctor-dashboard"),
    path("profile/<int:id>/", doctor_profile, name="doctor-profile"),
    path("appointments/", list_appointments, name="doctor-appointments"),
    path("patients/", list_assigned_patients, name="doctor-patients")
]