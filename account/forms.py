from django import forms









class RegisterationForm(forms.Form):
    pass



class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"placeholder": "Enter your email"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"}), min_length=6)

    class Media:
        css = {
            "css": ["css/login.css"]
        }
