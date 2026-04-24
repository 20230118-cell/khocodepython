import socket

host = "127.0.0.1"
port = 8091

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

a = input("Nhập a: ")
b = input("Nhập b: ")

msg = a + "," + b
s.send(msg.encode())

data = s.recv(1024).decode()
print("Tổng từ server:", data)

s.close()