# server.py
# This script listens for incoming encrypted UDP messages and decrypts them.

# Properties
# - sock: socket.socket
#     A UDP socket that listens for messages on IP:PORT
# - key: bytes
#     The shared encryption key used to decrypt received data

# Main Flow:
# 1. Load the encryption key from 'key.key'
# 2. Bind the socket to IP and PORT from config.py
# 3. Continuously wait for UDP packets using `sock.recvfrom()`
# 4. Decrypt each received message using `encryption.decrypt_message()`
# 5. Print the decrypted message (or error if decryption fails)

# Why this file matters:
# - This is the receiver in the communication loop
# - It handles decryption and displays messages from the client
# - Teaches:
#     - How to set up a server with UDP
#     - Safe decryption and error handling

# server.py
# Receives encrypted UDP messages and decrypts them

import socket
from encryption import decrypt_message, load_key
from config import IP, PORT

def main():
    key = load_key()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, PORT))

    print("Encrypted UDP Chat Server Listening...\n")

    while True:
        try:
            data, addr = sock.recvfrom(4096)
            decrypted = decrypt_message(data, key)
            print(f"[{addr}] {decrypted.decode()}")

        except Exception as e:
            print("Error receiving or decrypting:", e)

if __name__ == "__main__":
    main()
