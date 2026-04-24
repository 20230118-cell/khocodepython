import socket
import threading

host = "0.0.0.0"
port = 9000

server = socket.socket()
server.bind((host, port))
server.listen()

clients = []

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg, client)
        except:
            clients.remove(client)
            client.close()
            break

def broadcast(msg, sender):
    for client in clients:
        if client != sender:
            client.send(msg)

print("Server chat đang chạy...")

while True:
    client, addr = server.accept()
    print("Connected:", addr)

    clients.append(client)

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()