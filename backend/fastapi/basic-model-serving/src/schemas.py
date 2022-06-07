"""Schemas of fastapi server.

from https://fastapi.tiangolo.com/tutorial/body/
- Author: bono
- Email: qhsh9713@gmail.com
- Reference
https://stackoverflow.com/questions/64943693/what-are-the-best-practices-for-structuring-a-fastapi-project
"""
from pydantic import BaseModel, Field


class EncodedImage(BaseModel):
    """Definition of encoded imgae schemas."""

    image: str = Field(..., desciption="Base64 encoded image")


class PredOutput(BaseModel):
    """Definition of pred output"""

    pred: str = Field(..., description="prediction output")
