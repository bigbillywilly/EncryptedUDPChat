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
