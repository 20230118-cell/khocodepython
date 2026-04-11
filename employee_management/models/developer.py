from models.employee import Employee

class Developer(Employee):
    def __init__(self, employee_id: str, name: str, age: int, email: str, 
                 base_salary: float, programming_languages: list = None):
        super().__init__(employee_id, name, age, email, base_salary)
        self.programming_languages = programming_languages or []

    def calculate_salary(self) -> float:
        return self.base_salary + 1000 * len(self.programming_languages)

    def __str__(self):
        langs = ", ".join(self.programming_languages) if self.programming_languages else "Không có"
        return f"[Developer] {super().__str__()} | Ngôn ngữ: {langs}"