from django import forms
from .models import Employee, Company

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'salary', 'company']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields='__all__'