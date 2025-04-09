from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list_create, name='employee-list'),
    path('by-company/', views.employees_by_company, name='employees-by-company'),
]
