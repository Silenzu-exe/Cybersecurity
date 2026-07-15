import socket

HOST = "0.0.0.0"
PORT = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"AABBCCC\n", (HOST, PORT))

data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
