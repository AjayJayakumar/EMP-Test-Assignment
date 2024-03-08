from rest_framework import serializers

from emp.employee_management_system.models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            "id",
            "name"
        ]

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = [
            "timestamp",
            "last_updated"
        ]
        