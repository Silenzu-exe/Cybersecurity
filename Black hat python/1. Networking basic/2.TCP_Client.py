import socket

HOST = "www.google.com"
PORT = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#create socket object

client.connect((HOST, PORT))#connect the client

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") #send some data

response = client.recv(4096)#receive some data

print(response.decode())
client.close()


'''
--> GET / HTTP/1.1 — request line: method GET, path / (the root page), protocol version HTTP/1.1
--> Host: google.com — required header in HTTP/1.1, tells the server which site you want (one server/IP can host multiple domains)
--> \r\n — carriage-return + newline, HTTP's line-ending convention (not just \n)
--> The final \r\n\r\n (blank line) — this is the part that broke in your earlier version. It tells the server "headers are finished, this is the complete request" — without it, the server keeps waiting for more headers that never arrive.
'''
