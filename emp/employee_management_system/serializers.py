from rest_framework import serializers

from .models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = [
            'name',
            'employee_id',
            'title',
            'department',
        ]

    def get_department(self, instance):
        dep = instance.department.department
        return dep
