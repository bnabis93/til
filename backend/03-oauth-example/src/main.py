"""Basic oauth example fastapi.

from https://fastapi.tiangolo.com/tutorial/body/
- Author: bono
- Email: qhsh9713@gmail.com
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/healthcheck")
async def healthcheck() -> bool:
    """Server healthcheck."""
    return True


