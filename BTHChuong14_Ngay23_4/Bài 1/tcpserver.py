import socket

host = "26.101.82.1"
port = 8090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print("Server đang lắng nghe...")

conn, addr = s.accept()
print("Kết nối từ:", addr)

while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    print("Client gửi:", data)

    msg = "From SERVER TCP"
    conn.send(msg.encode())

conn.close()