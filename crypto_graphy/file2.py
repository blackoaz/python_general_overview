import base64
import os
from cryptography.hazmat.primitives import asymmetric
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes

# Generate a private key for use in the RSA algorithm
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

private_key = key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)

public_key = key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

# Check if the private and public key files already exist
if not os.path.exists("private_key.pem"):
    print("Creating private_key.pem and public_key.pem file")
    with open("private_key.pem", "wb") as f:
        f.write(private_key)

    with open("public_key.pem", "wb") as f:
        f.write(public_key)

# Load private key from PEM file
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )

# Load public key from PEM file
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
    )

# Encrypt the message using the public key
message = input("Enter a message to encrypt: ").encode()
encoded_message = base64.b64encode(message)

encrypted_message = public_key.encrypt(
    encoded_message,
    asymmetric.padding.OAEP(
        mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    )
)

#decrypt the message using the private key
decrypted_message = private_key.decrypt(
    encrypted_message,
    asymmetric.padding.OAEP(
        mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(), 
        label=None,
    )
)
decrypted_message = base64.b64decode(decrypted_message).decode()

private_key.decrypt(
    encrypted_message,
    asymmetric.padding.OAEP(
        mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    )
)

print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)