

class Employee:
    def __init__(self, name, employee_id, title):
        self.name = name
        self.employee_id = employee_id
        self.title = title
    
    def display_details(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Title: {self.title}"
    
    def __str__(self):
        return f"{self.name} - {self.employee_id}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print(f"{employee} not found in {self.name}.")
    
    def list_employees(self):
        return [employee.display_details() for employee in self.employees]

# Data structure for company
company = {}

def add_department(name):
    if name not in company:
        company[name] = Department(name)
        print(f"Department {name} added.")
    else:
        print(f"Department {name} already exists.")

def remove_department(name):
    if name in company:
        del company[name]
        print(f"Department {name} removed.")
    else:
        print(f"Department {name} not found.")

def display_departments():
    print("Departments:")
    for name, department in company.items():
        print(f"{name}: {', '.join(department.list_employees())}")

def display_menu():
    print("Employee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Add Department")
    print("4. Remove Department")
    print("5. Display Departments")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department_name = input("Enter department name: ")
            if department_name in company:
                employee = Employee(name, employee_id, title)
                company[department_name].add_employee(employee)
                print(f"Employee {name} added to department {department_name}.")
            else:
                print(f"Department {department_name} does not exist.")
        elif choice == "2":
            employee_name = input("Enter employee name: ")
            department_name = input("Enter department name: ")
            if department_name in company:
                employees = company[department_name].employees
                found = False
                for employee in employees:
                    if str(employee) == employee_name:
                        company[department_name].remove_employee(employee)
                        print(f"Employee {employee_name} removed from department {department_name}.")
                        found = True
                        break
                if not found:
                    print(f"Employee {employee_name} not found in department {department_name}.")
            else:
                print(f"Department {department_name} does not exist.")
        elif choice == "3":
            department_name = input("Enter department name: ")
            add_department(department_name)
        elif choice == "4":
            department_name = input("Enter department name: ")
            remove_department(department_name)
        elif choice == "5":
            display_departments()
        elif choice == "6":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
