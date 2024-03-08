from django.urls import path
from .views import DepartmentView, EmployeeDetailView

urlpatterns = [
    path('department/', DepartmentView.as_view(), name='department-list'),
    path('department/<int:department_id>/', DepartmentView.as_view(), name='department-details'),
    path('employee/', EmployeeDetailView.as_view(), name='employee-list-with-details'),
    path('employee/<int:employee_id>/', EmployeeDetailView.as_view(), name='employee-details')
]
