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


@app.post("/items")
async def helloworld(packet: DummyPacket) -> str:
    """Return Helloworld."""
    print(f"request : {packet}")
    return f"packet id : {packet.dummy_id} msg : {packet.msg}"
