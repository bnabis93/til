"""Basic oauth example fastapi.

- Author: bono
- Email: qhsh9713@gmail.com
"""


import json
import os
from typing import Any, Dict

from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi import FastAPI, Request
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse

###################
# Oauth setting
###################
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID') or None
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET') or None
SECRET_KEY = os.environ.get('SECRET_KEY') or None
if GOOGLE_CLIENT_ID is None or GOOGLE_CLIENT_SECRET is None:
    raise BaseException('Missing env variables')
if SECRET_KEY is None:
    raise BaseException("Missing SECRET_KEY")

auth_config = {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID, 'GOOGLE_CLIENT_SECRET': GOOGLE_CLIENT_SECRET}
starlette_config = Config(environ=auth_config)
oauth = OAuth(starlette_config)
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
)


# Create app
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)


###################
# APIs
###################


@app.get('/')
async def homepage(request: Request):
    """Root."""
    user = request.session.get('user')
    if user:
        data = json.dumps(user)
        html = (
            f'<pre>{data}</pre>'
            '<a href="/logout">logout</a>'
        )
        return HTMLResponse(html)
    return HTMLResponse('<a href="/login">login</a>')


@app.get("/healthcheck")
async def healthcheck() -> bool:
    """Server healthcheck."""
    return True


@app.get("/info")
async def show_info() -> dict[str, str]:
    """Show auth config info."""
    return auth_config


###################
# OAuth APIs
###########"########


@app.get("/login")
async def login(request : Request):
    """Oauth Login."""
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.get('/auth')
async def auth(request: Request) -> Dict[Any, Any]:
    """Auth api."""
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        return HTMLResponse(f'<h1>{error.error}</h1>')
    user = token.get("userinfo")
    if user:
        request.session['user'] = dict(user)
    return RedirectResponse(url='/')
