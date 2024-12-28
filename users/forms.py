from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'city', 'country', 'gender', 'marital_status', 'age', 'profile_picture']
        widgets = {
            'password': forms.PasswordInput(),
        }
