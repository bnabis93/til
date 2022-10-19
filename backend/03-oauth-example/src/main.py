"""Basic oauth example fastapi.

from https://fastapi.tiangolo.com/tutorial/body/
- Author: bono
- Email: qhsh9713@gmail.com
"""


import os

from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.config import Config

app = FastAPI()

###################
# Oauth setting
###################
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID') or None
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET') or None
if GOOGLE_CLIENT_ID is None or GOOGLE_CLIENT_SECRET is None:
    raise BaseException('Missing env variables')

auth_config =  {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID, 'GOOGLE_CLIENT_SECRET': GOOGLE_CLIENT_SECRET}
starlette_config = Config(environ=auth_config)
oauth = OAuth(starlette_config)
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
)



###################
# APIs
###################
@app.get("/healthcheck")
async def healthcheck() -> bool:
    """Server healthcheck."""
    return True
