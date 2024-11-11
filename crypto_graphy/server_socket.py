import socket
import base64
import os
from cryptography.hazmat.primitives import asymmetric
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
import time

# Create the server RSA key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Save the public key to be shared with the client
public_key = key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

# Start the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  # Bind to localhost on port 12345
server_socket.listen(1)
server_socket.settimeout(300)  # Set timeout for 5 minutes (300 seconds)

print("Server is listening on port 12345...")

try:
    conn, addr = server_socket.accept()
    conn.settimeout(300)  # Set individual connection timeout
    print(f"Connection from {addr} established.")

    # Send the public key to the client
    conn.send(public_key)

    while True:
        try:
            # Receive the encrypted message from the client
            encrypted_message = conn.recv(1024)
            if not encrypted_message:
                print("Client disconnected.")
                break

            # Decrypt the message using the server's private key
            decrypted_message = key.decrypt(
                encrypted_message,
                asymmetric.padding.OAEP(
                    mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                )
            )

            # Decode the decrypted message from base64
            decrypted_message = base64.b64decode(decrypted_message).decode()

            print("Decrypted message from client:", decrypted_message)

            # Echo the message back (optional)
            response_message = f"Received: {decrypted_message}".encode()
            conn.send(response_message)

        except socket.timeout:
            print("No interaction for 5 minutes. Closing connection.")
            break

except socket.timeout:
    print("Server timed out. No connection requests within 5 minutes.")

finally:
    conn.close()
    server_socket.close()
    print("Server closed.")
