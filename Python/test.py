import socket

HOST = "192.168.10.124"
PORT = 62078

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(3)  # don't hang forever waiting for a banner
client.connect((HOST, PORT))

try:
    client.send(b"HEllO\r\n")
    response = client.recv(4096)
    print(response.decode(errors="replace"))
except socket.timeout:
    print("[-] No response within timeout")
except ConnectionResetError:
    print("[-] Connection reset by peer — service rejected the input")

client.close()