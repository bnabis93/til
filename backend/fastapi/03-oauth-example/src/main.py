"""Basic oauth example fastapi.

- Author: bono
- Email: qhsh9713@gmail.com
"""


import json

import requests
from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse

from src.config import GOOGLE_CONF_URL, configs

# Create app
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="SECRET_KEY")
oauth = OAuth(configs)
oauth.register(
    name="google",
    server_metadata_url=GOOGLE_CONF_URL,
    client_kwargs={"scope": "openid email profile"},
)
###################
# APIs
###################


@app.get("/")
async def homepage(request: Request):
    """Root."""
    user = request.session.get("user")
    if user:
        data = json.dumps(user)
        html = f"<pre>{data}</pre>" '<a href="/logout">logout</a>'
        return HTMLResponse(html)
    return HTMLResponse('<a href="/login">login</a>')


@app.get("/healthcheck")
async def healthcheck() -> bool:
    """Server healthcheck."""
    return True


@app.get("/info")
async def info() -> dict[str, str]:
    """Show auth config info."""
    return {
        "GOOGLE_CLIENT_ID": configs("GOOGLE_CLIENT_ID"),
        "GOOGLE_CLIENT_SECRET": configs("GOOGLE_CLIENT_SECRET"),
    }


###################
# OAuth APIs
###########"########


@app.get("/login")
async def login(request: Request):
    """Login api."""

    # Redirect to /auth
    redirect_uri = request.url_for("auth")
    print("Redirection to /auth : ", redirect_uri)

    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.get("/auth")
async def auth(request: Request):
    """Auth."""

    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        return HTMLResponse(f"<h1>{error.error}</h1>")
    user = token.get("userinfo")
    print("user : ", user)
    if user:
        request.session["user"] = dict(user)
    return RedirectResponse(url="/")


@app.get("/logout")
async def logout(request: Request):
    """logout."""
    request.session.pop("user", None)
    return RedirectResponse(url="/")
