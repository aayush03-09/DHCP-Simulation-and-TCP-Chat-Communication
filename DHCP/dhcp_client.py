# dhcp_client.py
import socket
import json
import time

SERVER_IP = "10.21.22.56"
SERVER_PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Step 1: Send DISCOVER
client.sendto("DISCOVER".encode(), (SERVER_IP, SERVER_PORT))

# Step 2: Wait for OFFER
data, _ = client.recvfrom(1024)
offer = json.loads(data.decode())
offered_ip = offer["OFFER"]
print(f"📨 Got IP offer: {offered_ip}")

# Step 3: Send REQUEST
time.sleep(1)
client.sendto("REQUEST".encode(), (SERVER_IP, SERVER_PORT))

# Step 4: Receive ACK
data, _ = client.recvfrom(1024)
ack = json.loads(data.decode())
print(f"✅ IP {ack['ACK']} assigned successfully!")
