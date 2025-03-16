import requests
import json

url = "https://olimp.miet.ru/ppo_it/api"

tyles = list()
while len(tyles) != 16:
    resp = requests.get(url)
    if resp.status_code == 200:
        relief = resp.json()['message']['data']
        if relief not in tyles:
            tyles.append(relief)

            with open(f"../tyles_files/{len(tyles)}.json", "w") as f:
                json.dump(relief, f)
# for i, el in enumerate(tyles, 1):

