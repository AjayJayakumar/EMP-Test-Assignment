from django.urls import path
from .views import DepartmentView, EmployeeDetailView

urlpatterns = [
    path('department/', DepartmentView.as_view()),
    path('employee/', EmployeeDetailView.as_view())
]
