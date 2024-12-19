import socket

target = "192.168.124.128"
port = 81

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.setdefaulttimeout(1)

for port in range(1, 1000):
    try:
        result = s.connect((target, port))
        if result == None:
            print(f"Port {port}is open")
    except:
        print(f"Port {port} is closed")