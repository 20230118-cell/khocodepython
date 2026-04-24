import socket
import re

def check_pass(p):
    if len(p) < 6 or len(p) > 12:
        return False

    if not re.search("[a-z]", p):
        return False

    if not re.search("[A-Z]", p):
        return False

    if not re.search("[0-9]", p):
        return False

    if not re.search("[$#@]", p):
        return False

    return True


host = "0.0.0.0"
port = 8092

s = socket.socket()
s.bind((host, port))
s.listen(1)

print("Server đang chạy...")

conn, addr = s.accept()

while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    passwords = data.split(",")

    valid = []

    for p in passwords:
        if check_pass(p.strip()):
            valid.append(p.strip())

    result = ",".join(valid)
    conn.send(result.encode())

conn.close()