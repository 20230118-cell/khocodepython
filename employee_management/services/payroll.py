from models.employee import Employee
from services.company import Company

class Payroll:
    @staticmethod
    def calculate_total_salary(company: Company) -> float:
        return sum(emp.calculate_salary() for emp in company.employees)

    @staticmethod
    def get_top_3_highest_salary(company: Company):
        return sorted(company.employees, key=lambda e: e.calculate_salary(), reverse=True)[:3]

    @staticmethod
    def get_employee_count_by_type(company: Company):
        counts = {"Manager": 0, "Developer": 0, "Intern": 0}
        for emp in company.employees:
            if isinstance(emp, Manager): counts["Manager"] += 1
            elif isinstance(emp, Developer): counts["Developer"] += 1
            elif isinstance(emp, Intern): counts["Intern"] += 1
        counts["Tổng"] = len(company.employees)
        return counts

    @staticmethod
    def get_total_salary_by_type(company: Company):
        totals = {"Manager": 0.0, "Developer": 0.0, "Intern": 0.0}
        for emp in company.employees:
            if isinstance(emp, Manager):
                totals["Manager"] += emp.calculate_salary()
            elif isinstance(emp, Developer):
                totals["Developer"] += emp.calculate_salary()
            elif isinstance(emp, Intern):
                totals["Intern"] += emp.calculate_salary()
        return totals

    @staticmethod
    def get_average_projects_per_employee(company: Company) -> float:
        if not company.employees:
            return 0.0
        total_projects = sum(len(emp.projects) for emp in company.employees)
        return total_projects / len(company.employees)