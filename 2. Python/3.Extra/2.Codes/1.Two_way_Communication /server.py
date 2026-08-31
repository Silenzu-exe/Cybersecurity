import socket
import threading

def handle_client(client_socket, client_address):
    print(f"[*] Accept the connection from {client_address[0]}:{client_address[1]}")
    
    while True:
        request = client_socket.recv(4096)
        
        if not request:
            print(f"[*] Disconnecting form {client_address[0]}")
            break
        
        print(f"[*] Received message: {request.decode().strip()}")
        
        decode_msg = request.decode()
        if decode_msg.lower() == "exit":
            print(f"[*] Client request to exit!!")
            break
    
        message = input("send>")
        client_socket.send(message.encode())
        
        if message == "exit":
            break
    client_socket.close()
        
IP = "0.0.0.0"
PORT = 9998

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((IP, PORT))

server.listen(5)
print(f"[*] Server is listening on {IP}:{PORT}")

while True:
    client_socket, client_address = server.accept()
    thread = threading.Thread(target = handle_client, args = (client_socket, client_address))
    thread.start()