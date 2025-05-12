from django.db import models
from doctor.models import Doctor
from patient.models import Patient




class Appointment(models.Model):
    class Status(models.TextChoices):
        SCHEDULED = "scheduled"
        COMPLETETD = "completed"
        CANCELLED = "cancelled"
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor")
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status, default=Status.SCHEDULED)

    def __str__(self):
        return f"{self.patient} with Dr. {self.doctor} on {self.date}"

