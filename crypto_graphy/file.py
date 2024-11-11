import base64
import json

# The dictionary
name = {
    'name': 'Paulo',
    'number': 20,
    'amount': 3000
}

# Convert dictionary to a JSON string
json_name = json.dumps(name)

# Encode the JSON string to bytes
encoded_name = json_name.encode()

# Base64 encode the bytes
final_encode = base64.b64encode(encoded_name)

# Decode the base64 encoded bytes to string for display
print("Encoded:", final_encode.decode())

# To decode the base64 encoded string back to the original JSON string
decoded_bytes = base64.b64decode(final_encode)
decoded_name = decoded_bytes.decode()

# Print the decoded JSON string
print("Decoded:", decoded_name)




