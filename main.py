import requests
from datetime import datetime


USERNAME = "nutrotick"
TOKEN = "sdasdasdadsa"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Writing a book",
    "unit": "page(s)",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.today().strftime("%Y%m%d")
print(today)

value_config = {
    "date": today,
    "quantity": "10"
}

# response = requests.post(url=value_endpoint, json=value_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

update_data = {
    "quantity": "7"
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)

print(value_endpoint)
