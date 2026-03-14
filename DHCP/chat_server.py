import socket

SERVER_IP = "0.0.0.0"   # Listen on all interfaces
SERVER_PORT = 6000

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, SERVER_PORT))
server.listen(1)

print(f"💬 Chat Server running on port {SERVER_PORT}...")
print("Waiting for client to connect...")

conn, addr = server.accept()
print(f"🔗 Client connected from {addr}")

while True:
    # Receive message from client
    message = conn.recv(1024).decode()
    if not message:
        break

    print(f"Client: {message}")

    # Send reply
    reply = input("You: ")
    conn.send(reply.encode())

conn.close()
