import sqlite3

DB_NAME = "nhansu.db"

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nhansu(
        cccd TEXT PRIMARY KEY,
        hoten TEXT,
        ngaysinh TEXT,
        gioitinh TEXT,
        diachi TEXT
    )
    """)

    conn.commit()
    conn.close()


def get_all():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM nhansu")
    rows = cursor.fetchall()

    conn.close()
    return rows


def insert(cccd, hoten, ngaysinh, gioitinh, diachi):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO nhansu VALUES(?,?,?,?,?)",
        (cccd, hoten, ngaysinh, gioitinh, diachi)
    )

    conn.commit()
    conn.close()


def update(cccd, hoten, ngaysinh, gioitinh, diachi):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE nhansu
    SET hoten=?, ngaysinh=?, gioitinh=?, diachi=?
    WHERE cccd=?
    """,(hoten, ngaysinh, gioitinh, diachi, cccd))

    conn.commit()
    conn.close()


def delete(cccd):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM nhansu WHERE cccd=?", (cccd,))

    conn.commit()
    conn.close()


def search(keyword):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM nhansu
    WHERE cccd LIKE ?
    OR hoten LIKE ?
    OR diachi LIKE ?
    """,('%'+keyword+'%','%'+keyword+'%','%'+keyword+'%'))

    rows = cursor.fetchall()
    conn.close()

    return rows