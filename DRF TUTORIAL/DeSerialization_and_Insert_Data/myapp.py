import requests
import json


URL = 'http://127.0.0.1:8000/stu_create/'

data = {
    'name': 'Dheeraj',
    'roll': 4,
    'city': 'HISAR',
}

json_data = json.dumps(data)

req = requests.post(url=URL, data=json_data)

adata = req.json()

print(adata)
