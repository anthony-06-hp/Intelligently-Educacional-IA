# accounts/forms.py

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'full_name', 'mobile', 'email',
            'institution', 'degree', 'major', 'graduation_year', 'gpa',
            'date_of_birth', 'gender', 'country', 'city',
            'interests', 'profile_picture', 'avatar'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(choices=User.GENDER_CHOICES),
        }
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'password1', 'password2', 'role']
