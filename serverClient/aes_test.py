from cryptography.fernet import Fernet

# Step 1: Generate a key (in real apps, you save/share this securely)
# creates a secure encryption key
key = Fernet.generate_key()
#makes an encrytpor with that key
cipher = Fernet(key)

# Step 2: Encrypt a message
plaintext = "hello secure world"

#encrytpes the plaintext message
ciphertext = cipher.encrypt(plaintext.encode())
print("Encrypted:", ciphertext)

# Step 3: Decrypt the message
decrypted = cipher.decrypt(ciphertext)

print("Decrypted:", decrypted.decode())
