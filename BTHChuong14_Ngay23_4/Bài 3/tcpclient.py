import socket

host = "127.0.0.1"
port = 8092

s = socket.socket()
s.connect((host, port))

data = input("Nhập password (phân cách dấu phẩy): ")

s.send(data.encode())

result = s.recv(1024).decode()

print("Password hợp lệ:", result)

s.close()