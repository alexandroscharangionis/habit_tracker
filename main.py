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
    "id": "Graph1",
    "name": "Meditation graph",
    "unit": "min",
    "type": "int",
    "color": "shibafu"
}
requests.post()
