import socket

# Created a UDP socket (AF_INET = IPv4, SOCK_DGRAM = UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 # Binds the socket to an address and port
sock.bind(("localhost", 9999))

print("Server listening on port 9999...")
while True:
    # Waits to receive a message (blocking call)
    data, addr = sock.recvfrom(1024)
    # Prints the received message and the address of the sender
    print(f"Received from {addr}: {data.decode()}")
    