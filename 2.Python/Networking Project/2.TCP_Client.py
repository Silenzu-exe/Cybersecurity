import socket

HOST = "www.google.com"
PORT = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#create socket object

client.connect((HOST, PORT))#connect the client

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") #send some data

response = client.recv(4096)#receive some data

print(response.decode())
client.close()