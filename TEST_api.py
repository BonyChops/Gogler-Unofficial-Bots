import requests
import json

r = requests.get("https://bonychops.com/experiment/discord-police/api/getGoglerPoint.php")
data = json.loads(r.text)
for member in data['data'].values():
    print(f'"{member["name"]}、ポイント{member["point"]}は流石に多すぎて草wwwwwwww')