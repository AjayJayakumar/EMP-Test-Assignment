from django.db import models

# Model for Department
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department
    
# Model for Employee
class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

