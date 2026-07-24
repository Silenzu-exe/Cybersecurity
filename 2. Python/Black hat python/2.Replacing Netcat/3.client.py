import socket

HOST = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

while True:
    cmd = input("shell> ")
    client.send(cmd.encode())
    
    if cmd.lower() in ("quit", "exit"):
        break
    
    respond = client.recv(4096)
    print(respond.decode(errors = "replace"))
    
client.close()