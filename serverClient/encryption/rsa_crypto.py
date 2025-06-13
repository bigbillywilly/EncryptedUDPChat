# rsa_crypto.py
# 📌 Purpose: Generate, save, load, encrypt, and decrypt RSA keys
# Supports secure AES key exchange between client and server.

import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# -------------------------------
# 🔐 RSA Overview
# -------------------------------
# RSA is a public-key encryption algorithm.
# It allows clients to encrypt a message using the *public key*,
# which only the server (with the *private key*) can decrypt.
# Used in HTTPS to safely share secrets like AES session keys.

# -------------------------------
# 🔧 Key Generation
# -------------------------------
def generate_rsa_keys(private_key_filename="private.pem", public_key_filename="public.pem"):
    """
    Generate RSA key pair and save to PEM files.
    Default output is in the same folder where script runs.
    """
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    # Save private key
    with open(private_key_filename, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Save public key
    public_key = private_key.public_key()
    with open(public_key_filename, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

# -------------------------------
# 📂 Key Loading
# -------------------------------
def load_private_key(path=None):
    if path is None:
        # This points to "encryption/private.pem"
        current_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_dir, "private.pem")

    with open(path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)

def load_public_key(path=None):
    if path is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_dir, "public.pem")

    with open(path, "rb") as f:
        return serialization.load_pem_public_key(f.read())

# -------------------------------
# 🔒 Encryption / Decryption
# -------------------------------
def encrypt_with_public_key(public_key, message: bytes) -> bytes:
    """
    Encrypts data using RSA public key (usually an AES key).
    """
    return public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def decrypt_with_private_key(private_key, encrypted_data: bytes) -> bytes:
    """
    Decrypts RSA-encrypted data using the RSA private key.
    """
    return private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
