# config.py
# Stores configuration constants shared by both client and server

# Properties
# - IP: str
#     The IP address of the server (usually 'localhost' for local testing)
# - PORT: int
#     The port used by both client and server to communicate over UDP
# - BUFFER_SIZE: int
#     The maximum size of message packets that can be received (in bytes)

# Example:
# IP = 'localhost'
# PORT = 9999
# BUFFER_SIZE = 4096

# Why this file matters:
# - It prevents duplication of config values across files.
# - Easy to change if you move to a remote machine or change ports.
# - Makes the code more maintainable and readable.
