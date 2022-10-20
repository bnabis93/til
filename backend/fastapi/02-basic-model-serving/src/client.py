"""Simple client code.

from https://fastapi.tiangolo.com/tutorial/body/
- Author: bono
- Email: qhsh9713@gmail.com
"""
import argparse

import cv2
import requests

from ml.inference import inference
from utils import decode_from_bin, encode_from_cv2

parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str, required=True, help="Test data path")
parser.add_argument("--decode_test", default=0, type=int, help="Decoding test")
parser.add_argument(
    "--url", default="http://localhost:8000/pred", type=str, help="Fastapi url"
)


if __name__ == "__main__":
    args = parser.parse_args()
    image = cv2.cvtColor(cv2.imread(args.data), cv2.COLOR_BGR2RGB)
    height, width, *_ = image.shape
    encoded_image = encode_from_cv2(image)

    if args.decode_test == 1:
        print("Decoding test")
        decoded_image = decode_from_bin(encoded_image)
        cv2.imwrite("./test.jpeg", decoded_image)

        result = inference(decoded_image)
        print(result)
    req_body = {"image": encoded_image}
    req = requests.post(args.url, json=req_body)
    print(req.text)
