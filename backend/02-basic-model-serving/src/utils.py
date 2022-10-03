"""Utils code.

from https://fastapi.tiangolo.com/tutorial/body/
- Author: bono
- Email: qhsh9713@gmail.com
"""

import base64

import cv2
import numpy as np


def decode_from_bin(bin_data):
    "Decoding image"
    bin_data = base64.b64decode(bin_data)
    image = np.asarray(bytearray(bin_data), dtype=np.uint8)
    # Should change RGB formt
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return rgb_img


def encode_from_cv2(img):
    "Encoding image."
    bin = cv2.imencode(".jpg", img)[1]
    return str(base64.b64encode(bin), "utf-8")
