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
from encryption.rsa_crypto import load_private_key, decrypt_with_private_key
from config import IP, PORT

def main():
    # Load private key for decryption
    private_key = load_private_key()

    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((IP, PORT))
    print(f" Server is listening on {IP}:{PORT}")

    while True:
        try:
            # Receive data from client
            encrypted_data, addr = server_socket.recvfrom(4096)  # 4096 bytes max
            print(f"\nReceived encrypted message from {addr}")

            # Decrypt the message
            decrypted_message = decrypt_with_private_key(private_key, encrypted_data)
            print(f" Decrypted message: {decrypted_message.decode()}")

        except Exception as e:
            print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
