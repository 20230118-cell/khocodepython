from abc import ABC, abstractmethod
from exceptions.employee_exceptions import InvalidAgeError, InvalidSalaryError, ProjectAllocationError

class Employee(ABC):
    def __init__(self, employee_id: str, name: str, age: int, email: str, base_salary: float):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.email = email
        self.base_salary = base_salary
        self.performance_score = 0.0
        self.projects = []

    @abstractmethod
    def calculate_salary(self) -> float:
        pass

    def add_project(self, project_name: str):
        if len(self.projects) >= 5:
            raise ProjectAllocationError("Nhân viên đã tham gia tối đa 5 dự án")
        self.projects.append(project_name)

    def remove_project(self, project_name: str):
        if project_name in self.projects:
            self.projects.remove(project_name)

    def update_performance_score(self, score: float):
        if not 0 <= score <= 10:
            raise ValueError("Điểm hiệu suất phải trong khoảng 0-10")
        self.performance_score = score

    def __str__(self):
        projects_str = ", ".join(self.projects) if self.projects else "Không có"
        return (f"ID: {self.employee_id} | Tên: {self.name} | Tuổi: {self.age} | "
                f"Email: {self.email} | Lương CB: {self.base_salary:,.0f} | "
                f"Điểm HS: {self.performance_score} | Dự án: {projects_str}")