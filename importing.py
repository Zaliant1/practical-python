import requests

response = requests.get("https://api.open-notify.org/astros.json")
json = response.json()
print(json)

for person in json["people"]:
    print(person["name"])
