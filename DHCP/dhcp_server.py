# dhcp_server.py
import socket
import json

# Server settings
SERVER_IP = "0.0.0.0"      #this laptop ip address
SERVER_PORT = 5555

# IP pool (simulate 192.168.1.x)
ip_pool = [f"192.168.1.{i}" for i in range(10, 21)]
assigned_ips = {}

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER_IP, SERVER_PORT))
print("✅ DHCP Server running... Waiting for requests...")

while True:
    data, addr = server.recvfrom(1024)
    msg = data.decode()
    
    if msg == "DISCOVER":
        print(f"📡 Received DISCOVER from {addr}")
        if ip_pool:
            ip = ip_pool.pop(0)
            assigned_ips[addr] = ip
            offer = json.dumps({"OFFER": ip})
            server.sendto(offer.encode(), addr)
            print(f"💡 Offered IP {ip} to {addr}")
        else:
            server.sendto("NO_IP_AVAILABLE".encode(), addr)

    elif msg.startswith("REQUEST"):
        print(f"📩 Received REQUEST from {addr}")
        requested_ip = assigned_ips.get(addr)
        if requested_ip:
            ack = json.dumps({"ACK": requested_ip})
            server.sendto(ack.encode(), addr)
            print(f"✅ Assigned IP {requested_ip} to {addr}")

    elif msg == "RELEASE":
        ip = assigned_ips.pop(addr, None)
        if ip:
            ip_pool.append(ip)
            print(f"♻️ Released IP {ip} back to pool")
