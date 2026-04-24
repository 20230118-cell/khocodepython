import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

host = "127.0.0.1"
port = 9000

client = socket.socket()
client.connect((host, port))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            chat_area.insert(tk.END, msg + "\n")
        except:
            break

def send():
    msg = entry.get()
    client.send(msg.encode())
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Chat Client")

chat_area = scrolledtext.ScrolledText(window)
chat_area.pack()

entry = tk.Entry(window)
entry.pack(fill=tk.X)

btn = tk.Button(window, text="Send", command=send)
btn.pack()

thread = threading.Thread(target=receive)
thread.start()

window.mainloop()