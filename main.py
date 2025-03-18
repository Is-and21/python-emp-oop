# Main file
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, employee_id, name, department):
        self._employee_id = employee_id
        self._name = name
        self._department = department
    
    @abstractmethod
    def calculate_sal(self):
        pass
    
    def display_details(self):
        print("--- Employee Details ---")
        print(f"Employee ID: {self._employee_id}")
        print(f"Name: {self._name}")
        print(f"Department: {self._department}")


class PermanentEmployee(Employee):
    def __init__(self, employee_id, name, department, basic_salary, bonus):
        super().__init__(employee_id, name, department)
        self._basic_salary = basic_salary
        self._bonus = bonus
    
    def calculate_sal(self):
        return self._basic_salary + self._bonus
    
    def display_details(self):
        super().display_details()
        print(f"Basic Salary: ${self._basic_salary:.2f}")
        print(f"Bonus: ${self._bonus:.2f}")
        print(f"Total Salary: ${self.calculate_sal():.2f}\n")


class ContractEmployee(Employee):
    def __init__(self, employee_id, name, department, hourly_rate, hours_worked):
        super().__init__(employee_id, name, department)
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked
    
    def calculate_sal(self):
        return self._hourly_rate * self._hours_worked
    
    def display_details(self):
        super().display_details()
        print(f"Hourly Rate: ${self._hourly_rate:.2f}")
        print(f"Hours Worked: {self._hours_worked}")
        print(f"Total Salary: ${self.calculate_sal():.2f}\n")


class Intern(Employee):
    def __init__(self, employee_id, name, department, stipend):
        super().__init__(employee_id, name, department)
        self._stipend = stipend
    
    def calculate_sal(self):
        return self._stipend
    
    def display_details(self):
        super().display_details()
        print(f"Stipend: ${self._stipend:.2f}")
        print(f"Total Salary: ${self.calculate_sal():.2f}\n")


e1 = PermanentEmployee("P123", "Alice Johnson", "IT", 60000, 5000)
e2 = ContractEmployee("C456", "Bob Smith", "HR", 50, 160)
e3 = Intern("I789", "Charlie Brown", "Finance", 1500)


e1.display_details()
e2.display_details()
e3.display_details()
