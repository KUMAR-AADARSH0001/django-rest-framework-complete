"""This is a separate application. 
   It has nothing to do with Django, Derf, API or the like. 
   This application only comnicate with our API.
   This is only a third party Application."""
import requests
import json
URL = "http://127.0.0.1:8000/stu_info/list"


def get_data(id=None):
    data = {}
    if data is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    req = requests.get(url=URL, data=json_data)
    data = req.json()
    print(data)
