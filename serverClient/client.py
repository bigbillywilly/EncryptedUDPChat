import socket

# Creates a UDP socket (AF_INET = IPv4, SOCK_DGRAM = UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Sends a message to an IP + port (your server)
sock.sendto(b"Hello UDP Server!", ("localhost", 9999))
print("Message sent to UDP server on port 9999.") 