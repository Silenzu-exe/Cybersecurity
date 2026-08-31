import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Accept the connection form {client_address[0]}:{client_address[1]}")
    
    request = client_socket.recv(4096)
    print(f"[*]Request Received: {request.decode()}")
    
    client_socket.send(b"ACK from the server!!")
    client_socket.close()
    
IP = "0.0.0.0"
PORT = 9998
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((IP, PORT))

server.listen(5)
print("[*]Server is Listening on IP: 0.0.0.0, Port: 9998")

while True:
    client_socket, client_address = server.accept()
    client_thread = threading.Thread(
        target = handle_client, args = (client_socket, client_address)
    )
    client_thread.start()
  


