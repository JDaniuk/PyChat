import socket
from threading import Thread
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 50000  # The port used by the server

s = socket.socket()
print(f"Connecting to {HOST}:{PORT}")
s.connect((HOST, PORT))
nickname = input("Nickanme: ")
def listen():
    while True:
        message = s.recv(1024).decode()
        print("\n"+message)
t = Thread(target=listen)
t.daemon = True
t.start()
while True:
    user_message = input()
    to_send = nickname +": "+ user_message
    print(to_send)
    s.send(to_send.encode())