# encryption/aes_crypto.py
# AES-256 encryption and decryption utilities

import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# -------------------------------
# 🔐 AES Key Generation
# -------------------------------
def generate_aes_key():
    """
    Generate a secure 256-bit (32-byte) AES key.
    This key must be shared securely with the other party (e.g., via RSA encryption).
    """
    return os.urandom(32)

# -------------------------------
# 🔒 AES Encryption
# -------------------------------
def encrypt_aes(key: bytes, plaintext: str) -> str:
    """
    Encrypts a plaintext string using AES-256 in CBC mode.
    - Applies PKCS7 padding.
    - Generates a random IV.
    - Returns base64-encoded IV + ciphertext.
    """
    iv = os.urandom(16)  # 128-bit IV for CBC
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Combine IV and ciphertext and base64-encode them for safe transport
    return base64.b64encode(iv + ciphertext).decode()

# -------------------------------
# 🔓 AES Decryption
# -------------------------------
def decrypt_aes(key: bytes, encoded_data: str) -> str:
    """
    Decrypts base64-encoded IV + ciphertext string using AES-256 in CBC mode.
    - Separates IV from the beginning of the decoded bytes.
    - Removes PKCS7 padding.
    """
    raw_data = base64.b64decode(encoded_data.encode())
    iv = raw_data[:16]
    ciphertext = raw_data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode()
