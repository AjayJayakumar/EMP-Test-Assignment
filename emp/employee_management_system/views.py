from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentView(APIView):
    # To display the department list or a particular department details
    def get(self, request, department_id=None):
        if department_id:
            department = Department.objects.get(pk=department_id)
            serializer = DepartmentSerializer(department)
            return Response(serializer.data)
        else:
            departments = Department.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
            return Response(serializer.data)

    # To add a new department
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # To update an existing department
    def patch(self, request, pk):
        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise NotFound("Department not found")

        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # To delete an existing department
    def delete(self, request, pk):
        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise NotFound("department not found")

        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeDetailView(APIView):

    # To get details of an Employee or Employee list
    def get(self, request, employee_id=None):
        if employee_id:
            employee = Employee.objects.get(pk=employee_id)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data)

    # To add a new Employee
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # To update the details of existing Employee
    def patch(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise NotFound("Employee not found")

        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # To delete an existing Employee
    def delete(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise NotFound("Employee not found")

        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
