import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('<server-ip>', 5005))  # Replace with server's IP
print("Connected to server!")
client.close()