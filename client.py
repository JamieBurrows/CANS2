import socket
import sys
import server
IP = socket.gethostbyname((socket.gethostname()))
PORT = 4456
ADDR =(IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

HEADERSIZE = 10

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_sock.bind((ADDR))
srv_sock.listen(6)
HEADERSIZE = 10

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ADDR))
options = input("What would you like to choose? Upload, Download or Listing")
if options == "Upload":
    client.send(options.encode(FORMAT))
if options == "Download":
    client.send(options.encode(FORMAT))
if options == "Listing":
    client.send(options.encode(FORMAT))
print("LINE 19")
file = open("example.txt","r")
dataread = file.read()
client.send("example".encode(FORMAT))

msg = client.recv(SIZE)
client.send((dataread.encode(FORMAT)))
file.close()
while True:
    full_msg =""
    new_msg = True
    while True:
        msg = srv_sock.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
client.close()
