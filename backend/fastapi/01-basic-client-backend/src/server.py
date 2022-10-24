"""Basic example of fastapi.

from https://fastapi.tiangolo.com/tutorial/body/
- Author: bono
- Email: qhsh9713@gmail.com
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class DummyPacket(BaseModel):
    """Definition of dummy packet."""

    dummy_id: int
    msg: str


@app.get("/healthcheck")
def healthcheck() -> bool:
    """Server healthcheck api."""
    return True

@app.get("/helloworld")
def helloworld() -> str:
    """Simple helloworld api."""
    print("Helloworld in server side.")
    return "Helloworld response"

@app.post("/simplepost")
def simple_post(packet: DummyPacket) -> str:
    """Return Helloworld."""
    print(f"request server side : {packet}")
    return f"packet id : {packet.dummy_id} msg : {packet.msg}"
