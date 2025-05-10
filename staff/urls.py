from django.urls import path
from .views import (
    get_all_patient,
    get_one_patient,
    add_patient,
    delete_staff,
    update_staff,
    staff_dashboard

      )






urlpatterns = [
    path('', add_patient, name='add-patient'),
    path("all_patient/", get_all_patient,name = 'list-patient'),
    path('patient/<int:patient_id>/',get_one_patient, name='patient-detail'),
    path("patient/", update_staff),
    path('dashboard/', staff_dashboard, name='staff_dashboard'),

]
