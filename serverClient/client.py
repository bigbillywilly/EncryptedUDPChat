# client.py
# A secure UDP chat client that registers with the server and sends encrypted messages.

import socket
import threading
from encryption.rsa_crypto import (
    load_public_key, encrypt_with_public_key,
    generate_client_rsa_keys, load_client_public_key
)
from config import IP, PORT

# Global socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(("", 0))  # Let OS assign a random port
server_address = (IP, PORT)

def send_messages(server_pub_key):
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            break
        encrypted = encrypt_with_public_key(server_pub_key, message.encode())
        client_socket.sendto(encrypted, server_address)

def receive_messages():
    while True:
        try:
            data, _ = client_socket.recvfrom(4096)
            try:
                message = data.decode()
                print(f"\n[🔔] Message from server: {message}")
            except UnicodeDecodeError:
                print(f"\n[⚠️] Received non-text (binary) data: {data[:20]}...")
        except Exception as e:
            print(f"[❌] Error receiving: {e}")
            break


def main():
    # Step 0: Generate client RSA key pair if not already created
    generate_client_rsa_keys()

    # Step 1: Load server's public RSA key
    server_pub_key = load_public_key()

    # Step 2: Load our own public key to send to server
    client_pub_key_bytes = load_client_public_key()

    # Step 3: Send registration message to server
    register_message = b"REGISTER:" + client_pub_key_bytes
    client_socket.sendto(register_message, server_address)
    print("📬 Sent public key to server for registration.\n")

    print("✅ Connected to the secure chat.")
    print("Type messages and hit Enter to send. Type 'exit' to quit.\n")

    # Step 4: Start listening thread
    threading.Thread(target=receive_messages, daemon=True).start()

    # Step 5: Enter sending loop
    send_messages(server_pub_key)

    client_socket.close()

if __name__ == "__main__":
    main()
