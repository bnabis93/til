"""Simple client code.

- Author: bono
- Email: qhsh9713@gmail.com
"""

import json
import urllib

import requests

BACKEND_URL = "http://localhost:8000"
TARGET_URL = urllib.parse.urljoin(BACKEND_URL, "helloworld")

dummy_data = {"dummy_id": "3", "msg": "helloworld"}

response = requests.post(TARGET_URL, data=json.dumps(dummy_data))
print(f"response : {response.text}")
