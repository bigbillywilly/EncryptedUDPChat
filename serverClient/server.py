# server.py
import socket
import threading
from encryption.rsa_crypto import (
    load_private_key, decrypt_with_private_key,
    load_public_key_from_bytes, encrypt_with_public_key
)
from config import IP, PORT

# Dictionary to store {address: client_public_key}
client_keys = {}

# Load server's private RSA key
private_key = load_private_key()

# Setup UDP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((IP, PORT))
print(f"[🔐] Server listening on {IP}:{PORT}")

def handle_message(data: bytes, addr):
    global client_keys

    if addr not in client_keys and data.startswith(b"REGISTER:"):
        # Extract public key bytes
        client_pub_key_bytes = data[len("REGISTER:"):]
        try:
            client_keys[addr] = load_public_key_from_bytes(client_pub_key_bytes)
            print(f"[✅] Registered client {addr}")
        except Exception as e:
            print(f"[❌] Failed to load public key from {addr}: {e}")
        return

    if addr not in client_keys:
        print(f"[⚠️] Message from unregistered client {addr}. Ignoring.")
        return

    try:
        # Decrypt message from client
        decrypted = decrypt_with_private_key(private_key, data)
        print(f"[📩] From {addr}: {decrypted.decode()}")

        # Echo reply (re-encrypt with client’s public key)
        response = f"Received: {decrypted.decode()}".encode()
        encrypted_reply = encrypt_with_public_key(client_keys[addr], response)
        server_socket.sendto(encrypted_reply, addr)

    except Exception as e:
        print(f"[❌] Decryption or reply error: {e}")

def listen():
    while True:
        data, addr = server_socket.recvfrom(4096)
        threading.Thread(target=handle_message, args=(data, addr), daemon=True).start()

if __name__ == "__main__":
    listen()
