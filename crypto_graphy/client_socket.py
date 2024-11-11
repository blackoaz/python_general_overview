import socket
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Start the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # Connect to the server
client_socket.settimeout(300)  # Set timeout for 5 minutes (300 seconds)

# Receive the public key from the server
public_key = client_socket.recv(1024)

# Load the public key
public_key = serialization.load_pem_public_key(public_key)

try:
    while True:
        # Input the message from the user
        message = input("Enter a message to encrypt (or type 'exit' to quit): ")
        
        if message.lower() == "exit":
            print("Closing connection.")
            break

        encoded_message = base64.b64encode(message.encode())

        # Encrypt the message using the server's public key
        encrypted_message = public_key.encrypt(
            encoded_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            )
        )

        # Send the encrypted message to the server
        client_socket.send(encrypted_message)

        # Receive and print server's response
        response = client_socket.recv(1024)
        print(f"Server response: {response.decode()}")

except socket.timeout:
    print("No interaction for 5 minutes. Connection closed.")

finally:
    client_socket.close()
    print("Client closed.")
