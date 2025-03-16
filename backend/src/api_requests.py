import requests
import json

url = "https://olimp.miet.ru/ppo_it/api"


def get_all_tiles():
    tyles = list()
    while len(tyles) != 16:
        resp = requests.get(url)
        if resp.status_code == 200:
            relief = resp.json()['message']['data']
            if relief not in tyles:
                tyles.append(relief)

                with open(f"../tyles_files/{len(tyles)}.json", "w") as f:
                    json.dump(relief, f)


def get_coords() -> dict:
    while True:
        resp = requests.get(url + "/coords")
        if resp.status_code == 200:
            data = resp.json()['message']
            res = dict()
            res['listener'] = data['listener']
            res['sender'] = data['sender']
            res['price'] = data['price']
            return data


