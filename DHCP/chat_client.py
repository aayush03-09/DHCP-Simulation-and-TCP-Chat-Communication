import socket

SERVER_IP = "10.21.22.56"   # Replace with server laptop's IP
SERVER_PORT = 6000

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))

print("✅ Connected to server. You can start chatting.")

while True:
    # Send message to server
    msg = input("You: ")
    client.send(msg.encode())

    # Receive server reply
    reply = client.recv(1024).decode()
    print(f"Server: {reply}")
