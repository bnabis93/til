"""Simple client code.

from https://fastapi.tiangolo.com/tutorial/body/
- Author: bono
- Email: qhsh9713@gmail.com
"""
import argparse
import base64

import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str, required=True, help="Test data path")
parser.add_argument("--decode_test", default=0, type=int, help="Decoding test")


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


if __name__ == "__main__":
    args = parser.parse_args()
    image = cv2.cvtColor(cv2.imread(args.data), cv2.COLOR_BGR2RGB)
    height, width, *_ = image.shape
    encoded_image = encode_from_cv2(image)

    if args.decode_test == 1:
        print("Decoding test")
        decoded_image = decode_from_bin(encoded_image)
        cv2.imwrite("./test.jpeg", decoded_image)
