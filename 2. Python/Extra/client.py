import socket
import threading

HOST = "127.0.0.1"
PORT = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

def rev_loop(client):
    while True:
        respond = client.recv(4096)
    
        if not respond:
            print("[*] Server close the connection")
            break
    
        print(f"\n[*] Received message: {respond.decode()}\nsend> ", end="")
    
def send_loop():
    while True:
        message = input("send> ")
        client.send(message.encode())
        if message.lower() == "exit":
            break
    
        
recv_thread = threading.Thread(target = rev_loop, args = ((client, )), daemon= True)
recv_thread.start()
send_loop()
client.close()