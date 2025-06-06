# client.py
# This script acts as the sender. It encrypts messages and sends them via UDP.

# Properties (used internally)
# - sock: socket.socket
#     The UDP socket used to send messages to the server
# - server_address: tuple
#     Combines the IP and PORT into one destination

# Main Flow:
# 1. Load the key from 'key.key'
# 2. Repeatedly prompt the user for input (text messages)
# 3. Encrypt each message using `encryption.encrypt_message()`
# 4. Send the encrypted message to the server using `sock.sendto()`
# 5. User can type "exit" to quit the program

# Why this file matters:
# - It simulates a secure chat client sending data to a remote server.
# - Teaches how to:
#     - Use Python's socket module for UDP
#     - Securely transmit data
#     - Work with user input in loops
