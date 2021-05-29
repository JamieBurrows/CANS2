import socket
import sys
# Create socket
import client
IP = socket.gethostbyname((socket.gethostname()))
PORT = 4456
ADDR =(IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

HEADERSIZE = 10

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_sock.bind((ADDR))
srv_sock.listen(6)
print("server is listening")
while True:
    conn, address = srv_sock.accept()
    print(f"[NEW CONNECTION] {address} connection")
    filename = conn.recv(SIZE).decode(FORMAT)
    print("server is listening")
    if conn.recv() == "Upload":
        file = print(filename)
        file = open("example.txt" + filename, "w")
        conn.send("Filename received.".encode(FORMAT))
        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] File data received.")
        file.write(data)
        msg = "sheeeshhhhhhhhhhhhh"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        conn.send(bytes(msg, FORMAT))
        conn.send("File data received".encode(FORMAT))

        file.close()
        False
    if conn.recv() == "Download":
        file = open
        False
    if conn.recv() == "Listing":
        False

    file.close()
    conn.close()
    print(f"[DISCONNECTED] {address} disconnected")





