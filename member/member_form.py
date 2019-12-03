from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    userid = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User ID'}))
    email = forms.EmailField(max_length=256, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password Again'}))


    def check_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("The passwords do not match.")
        return password

class LoginForm(forms.Form):
    userid = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User ID'}))
    password = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



class MemberInfo(forms.Form):
    username = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
