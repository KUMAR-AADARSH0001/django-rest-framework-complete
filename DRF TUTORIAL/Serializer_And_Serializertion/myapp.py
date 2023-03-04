"""This is a separate application. 
   It has nothing to do with Django, Derf, API or the like. 
   This application only comnicate with our API.
   This is only a third party Application."""
import requests

URL = "http://127.0.0.1:8000/stu_info/list"

req = requests.get(url=URL)

data = req.json()

for i in data:
    print(i)
