# client.py
# Sends encrypted messages to a UDP server using RSA public key encryption.

import socket
from encryption.rsa_crypto import load_public_key, encrypt_with_public_key
from config import IP, PORT

# -------------------------------
# Main Client Function
# -------------------------------
def main():
    # Step 1: Load server's public RSA key from encryption/public.pem
    try:
        public_key = load_public_key()
    except FileNotFoundError:
        print("Public key file not found. Make sure encryption/public.pem exists.")
        return

    # Step 2: Initialize UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"Connected to {IP}:{PORT}")
    print("Type your messages below (type 'exit' to quit):\n")

    # Step 3: Loop to get input, encrypt, and send
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            print("[🔚] Exiting chat.")
            break

        try:
            # Step 4: Encrypt the message
            encrypted_message = encrypt_with_public_key(public_key, message.encode())

            # Step 5: Send to server
            client_socket.sendto(encrypted_message, (IP, PORT))

        except Exception as e:
            print(f"Failed to send message: {e}")

    client_socket.close()

if __name__ == "__main__":
    main()
