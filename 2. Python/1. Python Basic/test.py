import socket

HOST = "www.google.com"
PORT = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

respond = client.recv(4096)

print(respond.decode())
client.close()