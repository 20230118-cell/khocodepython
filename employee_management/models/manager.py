from models.employee import Employee

class Manager(Employee):
    def calculate_salary(self) -> float:
        return self.base_salary * 1.5

    def __str__(self):
        return f"[Manager] {super().__str__()}"