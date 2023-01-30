import requests

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
print(response.text)
