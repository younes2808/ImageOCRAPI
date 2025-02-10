import requests

# API endpoint (replace with your actual LocalTunnel URL)
url = "" # Change when localtunnel is on

# Path to the image file you want to send
image_path = "./036.png"

# Send the image using POST request
with open(image_path, "rb") as file:
    files = {"file": file}
    response = requests.post(url, files=files)

# Print the response (should return LaTeX code)
print(response.json())
