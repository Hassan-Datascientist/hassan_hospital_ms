from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from django.conf import settings

def send_assignment_email_html(to_email, doctor, patient, appointment_link):
    subject = "New Patient Assigned"
    context = {
        'doctor_name': f"{doctor.user.first_name} {doctor.user.last_name}",
        'patient_name': f"{patient.first_name} {patient.last_name}",
        'patient_gender': patient.gender,
        'assigned_date': timezone.now().strftime('%B %d, %Y'),
        'appointment_link': appointment_link,
        'current_year': timezone.now().year
    }

    html_content = render_to_string('emails/patient_assigned.html', context)
    text_content = strip_tags(html_content)  # Fallback for non-HTML clients

    email = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()