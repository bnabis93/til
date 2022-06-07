"""Basic example of fastapi.

from https://fastapi.tiangolo.com/tutorial/body/
- Author: bono
- Email: qhsh9713@gmail.com
- Referene : https://pydantic-docs.helpmanual.io/usage/schema/#field-customisation
"""


from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Inference(BaseModel):
    """Definition of dummy packet."""

    image: str = Field(..., desciption="Base64 encoded image")
    height: int = Field(..., description="Image's height")  # ... -> value is required
    width: str = Field(..., description="Image's width")


@app.get("/healthcheck")
def healthcheck() -> bool:
    """FastAPI server healthcheck."""
    return True


@app.get("/inference")
def inference() -> str:
    """Get inference result."""
    dummy: str = "cat"
    return dummy
