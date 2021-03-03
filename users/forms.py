from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from django.core.exceptions import ValidationError

def file_size(value):
    limit = 2 * 1024 * 1024 # 2 MiB
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MB.')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    image = forms.FileField(validators=[file_size])

    class Meta:
        model = Profile
        fields = ['image']