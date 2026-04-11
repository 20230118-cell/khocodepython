from models.employee import Employee
from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from exceptions.employee_exceptions import DuplicateEmployeeError, EmployeeNotFoundError

class Company:
    def __init__(self):
        self.employees: list[Employee] = []
        self.next_id = 1001

    def generate_new_employee_id(self) -> str:
        new_id = f"EMP{self.next_id}"
        self.next_id += 1
        return new_id

    def add_employee(self, employee: Employee):
        if any(e.employee_id == employee.employee_id for e in self.employees):
            raise DuplicateEmployeeError()
        self.employees.append(employee)

    def find_employee_by_id(self, employee_id: str) -> Employee:
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        raise EmployeeNotFoundError(employee_id)

    def remove_employee(self, employee_id: str):
        emp = self.find_employee_by_id(employee_id)
        self.employees.remove(emp)

    def search_by_name(self, name: str):
        return [e for e in self.employees if name.lower() in e.name.lower()]

    def search_developers_by_language(self, language: str):
        return [e for e in self.employees 
                if isinstance(e, Developer) and 
                any(language.lower() in lang.lower() for lang in e.programming_languages)]

    def get_employees_by_type(self, emp_type: str):
        if emp_type == "Manager":
            return [e for e in self.employees if isinstance(e, Manager)]
        elif emp_type == "Developer":
            return [e for e in self.employees if isinstance(e, Developer)]
        elif emp_type == "Intern":
            return [e for e in self.employees if isinstance(e, Intern)]
        return self.employees

    def get_employees_sorted_by_performance(self):
        return sorted(self.employees, key=lambda e: e.performance_score, reverse=True)