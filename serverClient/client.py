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


# client.py
# Sends encrypted messages to a server over UDP

import socket                    # For UDP communication
from encryption import encrypt_message, load_key  # Import your encryption tools
from config import IP, PORT     # Shared constants

def main():
    # Load the shared encryption key from file
    key = load_key()  # Returns bytes

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Encrypted UDP Chat Client Started!")
    print("Type 'exit' to quit.\n")

    while True:
        # Get a message from the user
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            # Convert string to bytes for encryption
            message_bytes = user_input.encode()

            # Encrypt the message
            encrypted = encrypt_message(message_bytes, key)

            # Send the encrypted message to the server
            sock.sendto(encrypted, (IP, PORT))

        except Exception as e:
            print("Something went wrong:", e)

if __name__ == "__main__":
    main()
