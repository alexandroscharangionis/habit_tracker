import requests
from datetime import datetime

USERNAME = "alexandroscharangionis"
TOKEN = "abcde12345"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Config parameters for Pixela graph
graph_config = {
    "id": "graph1",
    "name": "Meditation graph",
    "unit": "min",
    "type": "int",
    "color": "shibafu"
}

# Headers param for secure use of token (won't be displayed publicly via URL bar etc.):
headers = {
    "X-USER-TOKEN": TOKEN
}

# Create Pixela graph online:
response = requests.post(
    url=graph_endpoint, json=graph_config, headers=headers)

# Pixel creation endpoint:
pixel_creation_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()

pixel_creation_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "12"
}

# Create pixel on existing Pixela graph:
pixel_response = requests.post(
    url=pixel_creation_endpoint, json=pixel_creation_params, headers=headers)

# Update pixel on existing Pixela graph:
update_pixel_endpoint = f"{pixel_creation_endpoint}/20230129"
update_params = {
    "quantity": "25"
}
update_response = requests.put(
    url=update_pixel_endpoint, json=update_params, headers=headers)
print(update_response.text)

# Delete pixel:
delete_response = requests.delete(url=update_pixel_endpoint, headers=headers)
