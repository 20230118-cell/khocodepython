import sqlite3

# ===============================
# KẾT NỐI DATABASE
# ===============================
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# ===============================
# TẠO BẢNG (nếu chưa có)
# ===============================
cursor.execute("""
CREATE TABLE IF NOT EXISTS department(
    deptno INTEGER PRIMARY KEY,
    dname TEXT,
    loc TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee(
    empno INTEGER PRIMARY KEY,
    ename TEXT,
    job TEXT,
    mgr INTEGER,
    hiredate TEXT,
    sal REAL,
    comm REAL,
    deptno INTEGER,
    FOREIGN KEY(deptno) REFERENCES department(deptno)
)
""")

conn.commit()

# ===============================
# A. LẤY DANH SÁCH MANAGER
# ===============================
def cau_a():
    print("\n--- DANH SÁCH MANAGER ---")
    cursor.execute("SELECT * FROM employee WHERE job='MANAGER'")
    rows = cursor.fetchall()

    for row in rows:
        print(row)


# ===============================
# B. INSERT DEPARTMENT
# ===============================
def cau_b():
    print("\n--- INSERT DEPARTMENT ---")

    deptno = int(input("Nhập mã phòng: "))
    dname = input("Tên phòng: ")
    loc = input("Địa điểm: ")

    cursor.execute(
        "INSERT INTO department VALUES(?,?,?)",
        (deptno, dname, loc)
    )

    conn.commit()
    print("Đã thêm department!")


# ===============================
# C. INSERT EMPLOYEE (BẢN THÂN)
# ===============================
def cau_c():
    print("\n--- INSERT EMPLOYEE ---")

    empno = int(input("Empno: "))
    ename = input("Tên: ")
    job = input("Chức vụ: ")
    mgr = input("Manager (có thể bỏ trống): ")
    hiredate = input("Ngày vào (YYYY-MM-DD): ")
    sal = float(input("Lương: "))
    comm = input("Hoa hồng (có thể bỏ trống): ")
    deptno = int(input("Deptno: "))

    if mgr == "":
        mgr = None

    if comm == "":
        comm = None

    cursor.execute("""
    INSERT INTO employee
    VALUES(?,?,?,?,?,?,?,?)
    """, (empno, ename, job, mgr, hiredate, sal, comm, deptno))

    conn.commit()
    print("Đã thêm employee!")


# ===============================
# D. UPDATE CLARK -> THÔNG TIN BẠN
# ===============================
def cau_d():
    print("\n--- UPDATE CLARK ---")

    ename = input("Tên mới của bạn: ")
    job = input("Chức vụ: ")
    sal = float(input("Lương: "))

    cursor.execute("""
    UPDATE employee
    SET ename=?,
        job=?,
        sal=?
    WHERE ename='CLARK'
    """, (ename, job, sal))

    conn.commit()
    print("Đã cập nhật CLARK!")


# ===============================
# E. DELETE MILLER
# ===============================
def cau_e():
    print("\n--- DELETE MILLER ---")

    cursor.execute("DELETE FROM employee WHERE ename='MILLER'")
    conn.commit()

    print("Đã xóa MILLER!")


# ===============================
# MENU
# ===============================
while True:
    print("""
==============================
1. Câu A - Danh sách MANAGER
2. Câu B - Insert Department
3. Câu C - Insert Employee
4. Câu D - Update CLARK
5. Câu E - Delete MILLER
0. Thoát
==============================
""")

    chon = input("Chọn: ")

    if chon == "1":
        cau_a()

    elif chon == "2":
        cau_b()

    elif chon == "3":
        cau_c()

    elif chon == "4":
        cau_d()

    elif chon == "5":
        cau_e()

    elif chon == "0":
        break

conn.close()