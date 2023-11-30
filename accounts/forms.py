from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','age',)
    
    def age_restriction(self):
        age = self.cleaned_data.get('age')
        if age is not None and age <18:
            raise ValidationError(_('You must be at least 18 years old to register.'))
        return age

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','age',)
 