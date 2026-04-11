class EmployeeException(Exception):
    """Base exception cho hệ thống nhân viên"""
    pass

class EmployeeNotFoundError(EmployeeException):
    def __init__(self, employee_id):
        self.employee_id = employee_id
        super().__init__(f"Không tìm thấy nhân viên có ID: {employee_id}")

class InvalidSalaryError(EmployeeException):
    pass

class InvalidAgeError(EmployeeException):
    pass

class ProjectAllocationError(EmployeeException):
    pass

class DuplicateEmployeeError(EmployeeException):
    pass