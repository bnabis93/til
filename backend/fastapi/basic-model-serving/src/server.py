"""Basic example of fastapi.

from https://fastapi.tiangolo.com/tutorial/body/
- Author: bono
- Email: qhsh9713@gmail.com
- Referene : https://pydantic-docs.helpmanual.io/usage/schema/#field-customisation
"""

from fastapi import FastAPI

from src.schemas import Inference

app = FastAPI()


@app.get("/healthcheck")
def healthcheck() -> bool:
    """FastAPI server healthcheck."""
    return True


@app.get("/inference")
def inference() -> str:
    """Get inference result."""
    dummy: str = "cat"
    return dummy
