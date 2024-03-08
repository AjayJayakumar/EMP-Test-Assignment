from django.db import models


# Model for Department
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department


# Model for Company
class Company(models.Model):
    name = models.CharField(max_length=100)
    departments = models.ManyToManyField(Department)

    # Adds Department to the Company
    def add_department(self, department_name):
        department = Department.objects.get_or_create(department=department_name)
        self.departments.add(department)
        return department

    # Removes Department from the Company
    def remove_department(self, department_name):
        department = Department.objects.get(department=department_name)
        self.departments.remove(department)

    def display_departments(self):
        return self.departments.all()


# Model for Employee
class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
