from encryption.rsa_crypto import generate_rsa_keys
import os

# Get path to encryption folder
current_dir = os.path.dirname(os.path.abspath(__file__))
key_dir = os.path.join(current_dir, "encryption")

private_path = os.path.join(key_dir, "private.pem")
public_path = os.path.join(key_dir, "public.pem")

generate_rsa_keys(private_path, public_path)
print("[✅] RSA keys generated in encryption/")
