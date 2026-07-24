import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  #Translate hostname to IPv4
else:
    print("Invalid amount of arguments!")
    print("Syntax: python3 scanner.py <ip_address>")
    sys.exit(1)

#Add a banner
print("-" * 50)
print(f"Scanning target: {target}")
print("Time Started: " + str(datetime.now()))
print("-" * 50)
    
try: 
    for port in range(20, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open.")
        s.close()
except KeyboardInterrupt:
    print("\n Exiting program")
    sys.exit()

except socket.error:
    print("couldn't connect to the server")
    sys.exit()