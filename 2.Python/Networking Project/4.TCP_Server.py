import socket

IP = '0.0.0.0'
PORT = 9998

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind IP and PORT together
server.bind((IP, PORT))

server.listen(5) #Start Listening from upcoming connection
print(f"[*] Server is Listening on {IP}:{PORT}")

# Accept a connection(blocks untill someone connects)
client_socket, client_address = server.accept()
print(f"[*] Accept connection from {client_address[0]}:{client_address[1]}")

# Receive data from the client
request = client_socket.recv(4096)
print(f"[*] Received: {request.decode()}")

# Send a reply
client_socket.send(b"ACK from server!")

#closing
client_socket.close()
server.close()


'''
socket() — same as your client, just creating the raw socket object. No difference yet.
bind((IP, PORT)) — this is server-only. It claims a specific port on this machine so the OS knows "route traffic for port 9998 to me." 0.0.0.0 means "listen on all network interfaces," not just localhost — if you used 127.0.0.1 here, only connections from the same machine could reach it.
listen(5) — puts the socket into listening mode. The 5 is the backlog — how many pending connections can queue up before the OS starts rejecting new ones while you're busy handling one. Doesn't limit total connections, just the queue.
accept() — this is the big conceptual jump from your client code. It blocks (pauses execution) until a client actually connects. When one does, it returns two things: a new socket object specific to that one client (client_socket), and their address. This is the part that trips people up — you now have two sockets: the original server socket (still listening for more connections) and client_socket (for talking to this specific client).
client_socket.recv() — same as your TCP client's recv, just called on the per-client socket instead.
client_socket.send() — reply back to that specific client.
Close the per-client socket when done with them; close the server socket when you're shutting the whole thing down.
'''
