"""Basic example of fastapi.

from https://fastapi.tiangolo.com/tutorial/body/
- Author: bono
- Email: qhsh9713@gmail.com
- Referene : https://pydantic-docs.helpmanual.io/usage/schema/#field-customisation
"""
from fastapi import FastAPI

from src.ml.inference import inference
from src.schemas import EncodedImage, PredOutput
from src.utils import decode_from_bin

app = FastAPI()


@app.get("/healthcheck")
def healthcheck() -> bool:
    """FastAPI server healthcheck."""
    return True


@app.post("/pred")
def pred(encoded_image: EncodedImage) -> str:
    """Get inference result."""
    decoded_image = decode_from_bin(encoded_image.image)
    result = inference(decoded_image)
    return {"prediction": result}
