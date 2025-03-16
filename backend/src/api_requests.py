import requests
import json

def get_url():
    with open("./backend/src/url_addr.json", "rt", encoding="utf-8") as f:
        return json.load(f)['url']


def get_all_tiles():
    url = get_url()
    tyles = list()
    while len(tyles) != 16:
        resp = requests.get(url)
        if resp.status_code == 200:
            relief = resp.json()['message']['data']
            if relief not in tyles:
                tyles.append(relief)

                with open(f"../tyles_files/{len(tyles)}.json", "w") as f:
                    json.dump(relief, f)
    return tyles


def get_coords() -> dict:
    url = get_url()
    while True:
        resp = requests.get(url + "/coords")
        if resp.status_code == 200:
            data = resp.json()['message']
            res = dict()
            res['listener'] = data['listener']
            res['sender'] = data['sender']
            res['price'] = data['price']
            return data


