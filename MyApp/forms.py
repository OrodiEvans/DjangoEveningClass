from django import forms
from MyApp.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['firstname', 'lastname', 'email', 'password', 'age']
