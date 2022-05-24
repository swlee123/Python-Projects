import requests
import wget


account_id = 1064171348

## win lose of player

response = requests.get(f"https://api.opendota.com/api/players/{account_id}/wl")
player_data = response.json()

print(player_data)

## rank percentage


normal = requests.get(f"https://api.opendota.com/api/players/{account_id}")
rank = normal.json()["profile"]
url = rank["avatar"]
wget.download(url,"player_img.jpg")

print(rank)

