from django.db import models
from account.models import User



class Staff(models.Model):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('staff', 'Staff')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.role.capitalize()}"
