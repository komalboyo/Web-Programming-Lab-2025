from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Company
from .forms import EmployeeForm, CompanyForm

def employee_list_create(request):
    employees = Employee.objects.all()
    companies = Company.objects.all()

    emp_form = EmployeeForm()
    company_form = CompanyForm()

    if request.method == 'POST':
        # Create or Update Employee
        if 'action' in request.POST:
            action = request.POST['action']
            if action == 'create':
                emp_form = EmployeeForm(request.POST)
                if emp_form.is_valid():
                    emp_form.save()
                    return redirect('employee-list')

            elif action == 'update':
                emp_id = request.POST.get('emp_id')
                emp = get_object_or_404(Employee, id=emp_id)
                emp_form = EmployeeForm(request.POST, instance=emp)
                if emp_form.is_valid():
                    emp_form.save()
                    return redirect('employee-list')

            elif action == 'delete':
                emp_id = request.POST.get('emp_id')
                emp = get_object_or_404(Employee, id=emp_id)
                emp.delete()
                return redirect('employee-list')

        # Create or Update Company
        elif 'company_action' in request.POST:
            company_action = request.POST['company_action']
            if company_action == 'create':
                company_form = CompanyForm(request.POST)
                if company_form.is_valid():
                    company_form.save()
                    return redirect('employee-list')

            elif company_action == 'update':
                company_id = request.POST.get('company_id')
                company = get_object_or_404(Company, id=company_id)
                company_form = CompanyForm(request.POST, instance=company)
                if company_form.is_valid():
                    company_form.save()
                    return redirect('employee-list')

            elif company_action == 'delete':
                company_id = request.POST.get('company_id')
                company = get_object_or_404(Company, id=company_id)
                company.delete()
                return redirect('employee-list')

    return render(request, 'employee_list.html', {
        'employees': employees,
        'companies': companies,
        'emp_form': emp_form,
        'company_form': company_form,
    })



def employees_by_company(request):
    companies = Company.objects.all()
    selected_employees = []

    if request.method == 'POST':
        company_id = request.POST.get('company_id')
        selected_employees = Employee.objects.filter(company_id=company_id)

    return render(request, 'employees_by_company.html', {
        'companies': companies,
        'employees': selected_employees
    })
