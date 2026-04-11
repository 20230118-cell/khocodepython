import re
from exceptions.employee_exceptions import InvalidAgeError, InvalidSalaryError

def validate_age(age: int):
    if not (18 <= age <= 65):
        raise InvalidAgeError("Tuổi phải nằm trong khoảng 18-65")

def validate_salary(salary: float):
    if salary <= 0:
        raise InvalidSalaryError("Lương phải lớn hơn 0")

def validate_email(email: str):
    if '@' not in email:
        raise ValueError("Email không hợp lệ (phải có @)")
    # Kiểm tra định dạng cơ bản
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Email không đúng định dạng")

def validate_performance_score(score: float):
    if not 0 <= score <= 10:
        raise ValueError("Điểm hiệu suất phải trong khoảng 0-10")