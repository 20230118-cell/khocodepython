import socket

host = "26.101.82.1"
port = 8090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

msg = "From CLIENT TCP"
s.send(msg.encode())

data = s.recv(1024).decode()
print("Server trả về:", data)

s.close()