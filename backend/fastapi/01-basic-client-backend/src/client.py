"""Simple client code.

- Author: bono
- Email: qhsh9713@gmail.com
"""

import json
import urllib

import requests

BACKEND_URL = "http://localhost:8000"
TARGET_URL = urllib.parse.urljoin(BACKEND_URL, "helloworld")
TARGET_URL02 = urllib.parse.urljoin(BACKEND_URL, "simplepost")

response = requests.get(TARGET_URL)
print(f"get_response : {response.text}")

dummy_data = {"dummy_id": "3", "msg": "simple post example"}

response = requests.post(TARGET_URL02, data=json.dumps(dummy_data))
print(f"post response : {response.text}")
