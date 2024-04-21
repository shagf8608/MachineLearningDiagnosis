from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class PatientDataForm(forms.Form):
    Patient_ID = forms.IntegerField(label='Patient_ID')
    Pregnancies = forms.IntegerField(label='Pregnancies')
    Glucose = forms.DecimalField(label='Glucose')
    BloodPressure = forms.DecimalField(label='BloodPressure')
    SkinThickness = forms.DecimalField(label='SkinThickness')
    Insulin = forms.DecimalField(label='Insulin')
    BMI = forms.DecimalField(label='BMI')
    DiabetesPedigreeFunction = forms.DecimalField(label='DiabetesPedigreeFunction')
    Age = forms.IntegerField(label='Age')
