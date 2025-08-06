import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5005))  # Bind to all interfaces
server.listen(1)
print("Server listening on port 5005...")
conn, addr = server.accept()
print(f"Connection established with {addr}")
conn.close()