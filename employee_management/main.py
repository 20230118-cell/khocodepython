from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from services.company import Company
from services.payroll import Payroll
from utils.validators import validate_age, validate_salary, validate_email, validate_performance_score
from utils.formatters import format_employee_list
from exceptions.employee_exceptions import (
    DuplicateEmployeeError,
    EmployeeNotFoundError,
    InvalidAgeError,
    InvalidSalaryError
)

def main():
    company = Company()
    print("=== HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY ABC ===\n")

    while True:
        print("""1. Thêm nhân viên mới
2. Hiển thị danh sách nhân viên
3. Tìm kiếm nhân viên
4. Quản lý lương
5. Quản lý dự án
6. Đánh giá hiệu suất
7. Quản lý nhân sự
8. Thống kê báo cáo
9. Thoát""")
        
        try:
            choice = int(input("\nChọn chức năng (1-9): "))
            if not 1 <= choice <= 9:
                raise ValueError
        except ValueError:
            print("❌ Lựa chọn không hợp lệ! Vui lòng nhập số từ 1-9.")
            continue

        # 1. THÊM NHÂN VIÊN
        if choice == 1:
            print("a. Thêm Manager\nb. Thêm Developer\nc. Thêm Intern")
            sub = input("Chọn loại (a/b/c): ").lower().strip()
            try:
                name = input("Nhập tên: ").strip()
                age = int(input("Nhập tuổi: "))
                validate_age(age)
                email = input("Nhập email: ").strip()
                validate_email(email)
                base_salary = float(input("Nhập lương cơ bản: "))
                validate_salary(base_salary)

                emp_id = input("Nhập ID (để trống → tự sinh): ").strip()
                if not emp_id:
                    emp_id = company.generate_new_employee_id()

                if sub == 'a':
                    emp = Manager(emp_id, name, age, email, base_salary)
                elif sub == 'b':
                    langs_input = input("Ngôn ngữ lập trình (cách nhau bằng dấu phẩy): ")
                    langs = [lang.strip() for lang in langs_input.split(',') if lang.strip()]
                    emp = Developer(emp_id, name, age, email, base_salary, langs)
                elif sub == 'c':
                    emp = Intern(emp_id, name, age, email, base_salary)
                else:
                    print("❌ Loại không hợp lệ!")
                    continue

                company.add_employee(emp)
                print(f"✅ Thêm nhân viên thành công! ID: {emp.employee_id}")

            except DuplicateEmployeeError:
                print("⚠️ ID trùng → Tự động sinh ID mới")
                if 'emp' in locals():
                    emp.employee_id = company.generate_new_employee_id()
                    company.add_employee(emp)
                    print(f"✅ Thêm thành công với ID mới: {emp.employee_id}")
            except (InvalidAgeError, InvalidSalaryError, ValueError) as e:
                print(f"❌ Lỗi dữ liệu: {e}")
            except Exception as e:
                print(f"❌ Lỗi: {e}")

        # 2. HIỂN THỊ DANH SÁCH
        elif choice == 2:
            print("a. Tất cả\nb. Theo loại\nc. Theo hiệu suất cao → thấp")
            sub = input("Chọn (a/b/c): ").lower().strip()
            if sub == 'a':
                emps = company.employees
            elif sub == 'b':
                print("1.Manager  2.Developer  3.Intern")
                t = input("Chọn số: ").strip()
                typemap = {"1": "Manager", "2": "Developer", "3": "Intern"}
                emps = company.get_employees_by_type(typemap.get(t, ""))
            elif sub == 'c':
                emps = company.get_employees_sorted_by_performance()
            else:
                emps = []
            print("\n" + format_employee_list(emps))

        # 3. TÌM KIẾM
        elif choice == 3:
            print("a. Theo ID\nb. Theo tên\nc. Theo ngôn ngữ (Developer)")
            sub = input("Chọn (a/b/c): ").lower().strip()
            if sub == 'a':
                eid = input("Nhập ID: ").strip()
                try:
                    emp = company.find_employee_by_id(eid)
                    print(emp)
                except EmployeeNotFoundError as e:
                    print(e)
            elif sub == 'b':
                name = input("Nhập tên: ").strip()
                emps = company.search_by_name(name)
                print(format_employee_list(emps))
            elif sub == 'c':
                lang = input("Nhập ngôn ngữ: ").strip()
                emps = company.search_developers_by_language(lang)
                print(format_employee_list(emps))

        # 4. QUẢN LÝ LƯƠNG
        elif choice == 4:
            print("a. Tính lương từng người\nb. Tổng lương công ty\nc. Top 3 lương cao nhất")
            sub = input("Chọn (a/b/c): ").lower().strip()
            if sub == 'a':
                for emp in company.employees:
                    print(f"{emp.employee_id} - {emp.name}: {emp.calculate_salary():,.0f} VND")
            elif sub == 'b':
                total = Payroll.calculate_total_salary(company)
                print(f"Tổng lương toàn công ty: {total:,.0f} VND")
            elif sub == 'c':
                top = Payroll.get_top_3_highest_salary(company)
                print(format_employee_list(top))

        # 5. QUẢN LÝ DỰ ÁN
        elif choice == 5:
            print("a. Phân công dự án\nb. Xóa dự án\nc. Xem dự án của nhân viên")
            sub = input("Chọn (a/b/c): ").lower().strip()
            eid = input("Nhập ID nhân viên: ").strip()
            try:
                emp = company.find_employee_by_id(eid)
                if sub == 'a':
                    proj = input("Tên dự án: ").strip()
                    emp.add_project(proj)
                    print("✅ Phân công thành công!")
                elif sub == 'b':
                    proj = input("Tên dự án cần xóa: ").strip()
                    emp.remove_project(proj)
                    print("✅ Đã xóa dự án!")
                elif sub == 'c':
                    print("Dự án hiện tại:", emp.projects if emp.projects else "Không có dự án nào")
            except Exception as e:
                print(e)

        # 6. ĐÁNH GIÁ HIỆU SUẤT
        elif choice == 6:
            print("a. Cập nhật điểm\nb. Nhân viên xuất sắc (>8)\nc. Nhân viên cần cải thiện (<5)")
            sub = input("Chọn (a/b/c): ").lower().strip()
            if sub == 'a':
                eid = input("Nhập ID: ").strip()
                try:
                    emp = company.find_employee_by_id(eid)
                    score = float(input("Điểm hiệu suất (0-10): "))
                    validate_performance_score(score)
                    emp.update_performance_score(score)
                    print("✅ Cập nhật điểm thành công!")
                except Exception as e:
                    print(e)
            elif sub == 'b':
                emps = [e for e in company.employees if e.performance_score > 8]
                print(format_employee_list(emps))
            elif sub == 'c':
                emps = [e for e in company.employees if e.performance_score < 5]
                print(format_employee_list(emps))

        # 7. QUẢN LÝ NHÂN SỰ
        elif choice == 7:
            print("a. Xóa nhân viên\nb. Tăng lương cơ bản\nc. Thăng chức")
            sub = input("Chọn (a/b/c): ").lower().strip()
            eid = input("Nhập ID nhân viên: ").strip()
            try:
                if sub == 'a':
                    company.remove_employee(eid)
                    print("✅ Đã xóa nhân viên!")
                elif sub == 'b':
                    emp = company.find_employee_by_id(eid)
                    amount = float(input("Số tiền tăng lương: "))
                    emp.base_salary += amount
                    print(f"✅ Lương mới: {emp.base_salary:,.0f} VND")
                elif sub == 'c':
                    emp = company.find_employee_by_id(eid)
                    print(f"Chức vụ hiện tại: {type(emp).__name__}")
                    if isinstance(emp, Intern):
                        langs_input = input("Ngôn ngữ lập trình (cách nhau bằng phẩy): ")
                        langs = [l.strip() for l in langs_input.split(',') if l.strip()]
                        new_emp = Developer(emp.employee_id, emp.name, emp.age, emp.email, emp.base_salary, langs)
                    elif isinstance(emp, Developer):
                        new_emp = Manager(emp.employee_id, emp.name, emp.age, emp.email, emp.base_salary)
                    else:
                        print("❌ Không thể thăng chức Manager!")
                        continue
                    new_emp.performance_score = emp.performance_score
                    new_emp.projects = emp.projects[:]
                    company.remove_employee(eid)
                    company.add_employee(new_emp)
                    print("✅ Thăng chức thành công!")
            except Exception as e:
                print(e)

        # 8. THỐNG KÊ BÁO CÁO
        elif choice == 8:
            print("a. Số lượng theo loại\nb. Tổng lương theo loại\nc. Số dự án trung bình")
            sub = input("Chọn (a/b/c): ").lower().strip()
            if sub == 'a':
                print(Payroll.get_employee_count_by_type(company))
            elif sub == 'b':
                print(Payroll.get_total_salary_by_type(company))
            elif sub == 'c':
                avg = Payroll.get_average_projects_per_employee(company)
                print(f"Số dự án trung bình mỗi nhân viên: {avg:.2f}")

        # 9. THOÁT
        elif choice == 9:
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break

if __name__ == "__main__":
    main()