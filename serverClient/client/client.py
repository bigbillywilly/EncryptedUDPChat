import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b"Hello UDP Server!", ("localhost", 9999))
print("Message sent to UDP server on port 9999.") 