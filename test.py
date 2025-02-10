import requests
from urllib.parse import urljoin

# Base API URL (Change this as needed)
base_url = "https://slick-papers-beam.loca.lt/"

# "/upload" is appended after the url
upload_url = urljoin(base_url.rstrip("/") + "/", "upload")

# Path to the image file
image_path = "./058.png"

# Send the image using POST request
with open(image_path, "rb") as file:
    files = {"file": file}
    response = requests.post(upload_url, files=files)

# Print the response (should return LaTeX code)
print(response.json())
