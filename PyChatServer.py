import socket
from threading import Thread
from threading import active_count
HOST = "0.0.0.0"  # The server's hostname or IP address
PORT = 50000  # The port used by the server

client_sockets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
print(f"[*] Listening as {HOST}:{PORT}")

def user_thread(conn, addr):
    conn.send((f"Welcome {conn}").encode())
    run_thread = True
    while run_thread:
        try:
            msg = conn.recv(1024).decode()
            if msg:
                print(f"{addr[0]} sent message: {msg}")
                for client in client_sockets:
                    if client != conn: # new change
                        try:
                            client.send(msg.encode())
                        except:
                            client.close()
                            client_sockets.remove(client)
        except:
            print(f"[!] Error")
            client_sockets.remove(conn)
            run_thread = False;
            
        

        
        
while True:
    conn, addr = s.accept()
    print(f"[+] {addr} connected.")
    client_sockets.add(conn)
    print(len(client_sockets))
    print(active_count())
    t = Thread(target=user_thread,args=(conn,addr))
    t.deamon = True
    t.start()
