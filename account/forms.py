from django import forms
from account.models import User
from staff.models import Staff
from doctor.models import Doctor

class StaffRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input'}),
            'last_name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.TextInput(attrs={'class': 'input'}),
            
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True  # optional: mark user active
        if commit:
            user.save()
            Staff.objects.create(user=user, role='staff')
        return user


class DoctorRegistrationForm(forms.ModelForm):
    # User fields
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # Doctor-specific fields are included via the model (specialization, available)

    class Meta:
        model = Doctor
        fields = ['specialization']

    def save(self, commit=True):
        # Create the user first
        user = User(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            is_doctor=True
        )
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        # Now create the doctor instance
        doctor = super().save(commit=False)
        doctor.user = user
        if commit:
            doctor.save()

        return doctor










class RegisterationForm(forms.Form):
    pass



class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"placeholder": "Enter your email"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"}), min_length=6)

    class Media:
        css = {
            "css": ["css/login.css"]
        }

