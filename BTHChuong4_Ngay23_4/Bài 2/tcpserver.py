import socket

host = "0.0.0.0"
port = 8091

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print("Server đang chạy...")

conn, addr = s.accept()
print("Connected:", addr)

while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    a, b = data.split(",")
    tong = int(a) + int(b)

    print("Nhận:", a, b)
    print("Tổng:", tong)

    conn.send(str(tong).encode())

conn.close()