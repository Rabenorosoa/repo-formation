from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accountsApp.models import Profile



class LoginForm(AuthenticationForm):
    username= forms.CharField(label = 'Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password= forms.CharField(label = 'Password' , widget=forms.PasswordInput(attrs={'class': 'form-control'})) 


class UserForm(UserCreationForm):
    username= forms.CharField(label = 'Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email= forms.CharField(label = 'Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1= forms.CharField(label = 'Password' , widget=forms.PasswordInput(attrs={'class': 'form-control'})) 
    password2= forms.CharField(label = 'Password' , widget=forms.PasswordInput(attrs={'class': 'form-control'})) 
    class Meta :
        model = User
        fields = ('username','email','password1','password2')

class ProfileForm(forms.ModelForm):
    birthday= forms.DateField(label = 'Birthday', widget=forms.DateInput(attrs={
        'class': 'form-control' , 'type': 'date'}
                ))
    phonenumber= forms.IntegerField(label = 'Phone Number', widget=forms.DateInput(attrs={
        'class': 'form-control' , 'type': 'number'}
                ))
    class Meta:
        model = Profile
        fields =('birthday', 'phonenumber')