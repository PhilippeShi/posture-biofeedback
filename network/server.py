import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        data_length = conn.recv(HEADER).decode(FORMAT) # 1024 is the header size (msg size)
        if data_length: # when connecting to the server, the data_length is empty
            data_length = int(data_length)
            data = conn.recv(data_length).decode(FORMAT)
            if data == "quit" or data == DISCONNECT_MESSAGE:
                connected = False
            else:
                print(f"[{addr}] {data}")
                conn.send(data.encode(FORMAT))
    conn.close()
    print(f"[CLOSED CONNECTION] {addr} disconnected.")


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] Server is starting...")
start()
