import requests

base_url = "http://localhost:3000"

def get_driver():
    res = requests.get(base_url + "/drivers")
    return res.json()

def add_driver(driver_data):
    res = requests.post(base_url + "/drivers", json=driver_data)
    return res.json()

def update_driver(driver_id, update_data):
    res = requests.put(base_url + f"/drivers/{driver_id}", json=update_data)
    return res.json()
    
def delete_driver(driver_id):
    res = requests.delete(base_url + f"/drivers/{driver_id}")
    return res.status_code
