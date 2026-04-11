def format_employee_list(employees):
    if not employees:
        return "Chưa có dữ liệu nhân viên nào."
    return "\n".join([f"{i+1}. {emp}" for i, emp in enumerate(employees)])