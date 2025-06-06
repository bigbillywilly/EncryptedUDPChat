# encryption.py
# Handles all encryption/decryption using AES (via Fernet)

# Properties
# - key_filename: string = 'key.key'
#     Location of the shared encryption key (used by both client and server)

# Methods
# - generate_key(filename='key.key')
#     Generates a strong random key and writes it to disk
# - load_key(filename='key.key') -> bytes
#     Loads the key so it can be reused for every message
# - encrypt_message(message: bytes, key: bytes) -> bytes
#     Converts a message into ciphertext using the key
# - decrypt_message(token: bytes, key: bytes) -> bytes
#     Converts ciphertext back into the original plaintext

# Why this file matters:
# - It centralizes the encryption logic so client/server can focus on networking.
# - It uses secure practices like Fernet under the hood (built on AES-128).

from cryptography.fernet import Fernet

# Generates a new key and saves it to 'key.key'
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

# Loads the key from 'key.key'
def load_key():
    with open("key.key", "rb") as f:
        return f.read()

# Encrypts a message using the key
def encrypt_message(message_bytes, key):
    f = Fernet(key)
    return f.encrypt(message_bytes)

# Decrypts a message using the key
def decrypt_message(encrypted_bytes, key):
    f = Fernet(key)
    return f.decrypt(encrypted_bytes)

