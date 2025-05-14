from django.urls import path
from .views import get_one_patient








urlpatterns = [
    path("<int:patient_id>/", get_one_patient, name="patient-info")
]