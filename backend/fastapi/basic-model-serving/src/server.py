"""Basic example of fastapi.

from https://fastapi.tiangolo.com/tutorial/body/
- Author: bono
- Email: qhsh9713@gmail.com
- Referene : https://pydantic-docs.helpmanual.io/usage/schema/#field-customisation
"""

import json

import cv2
from fastapi import FastAPI

from src.schemas import EncodedImage
from src.utils import decode_from_bin

app = FastAPI()


@app.get("/healthcheck")
def healthcheck() -> bool:
    """FastAPI server healthcheck."""
    return True


@app.post("/inference", response_model=EncodedImage)
def inference(encoded_image: EncodedImage) -> str:
    """Get inference result."""
    decoded_image = decode_from_bin(encoded_image.image)
    cv2.imwrite("./test2.jpeg", decoded_image)

    return None
