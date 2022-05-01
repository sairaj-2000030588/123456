from django import forms
from django.forms import TextInput
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'password']
        labels = {'name': 'Enter name', 'password': 'password'}
