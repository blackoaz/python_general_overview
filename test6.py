import requests

def download_file(url, save_path):
    # Send GET request to the URL
    response = requests.get(url, stream=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open a file in binary write mode
        with open(save_path, 'wb') as file:
            # Write the response content to the file in chunks
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded successfully and saved to {save_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

# URL of the file or image you want to download
url = 'https://images.unsplash.com/photo-1730483962596-f3e033866a59?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw3fHx8ZW58MHx8fHx8'
# Path to save the downloaded file
save_path = 'image.jpg'

# Download the file
download_file(url, save_path)
