import requests

base_url = "http://localhost:3000"

def get_race():
    res = requests.get(base_url + "/races")
    return res.json()

def add_race(race_data):
    res = requests.post(base_url + "/races", json=race_data)
    return res.json()

def update_race(race_id, update_data):
    res = requests.put(base_url + f"/races/{race_id}", json=update_data)
    return res.json()

def delete_race(race_id):
    res = requests.delete(base_url + f"/races/{race_id}")
    return res.status_code

                                                                                                                               


