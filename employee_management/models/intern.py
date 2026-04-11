from models.employee import Employee

class Intern(Employee):
    def calculate_salary(self) -> float:
        return self.base_salary * 0.6

    def __str__(self):
        return f"[Intern] {super().__str__()}"