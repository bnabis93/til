# Fastapi Oauth2.0 example (Google login)

## Create Google credential for oauto 2.0
- https://console.cloud.google.com/apis/dashboard?project=storied-depot-334607
- Google is resource server.
1. Go to Credentials on the side panel.
2. Go to Create Credentials -> OAuth client ID.
3. We need to set up the consent screen, so we are going to set the User type to `External.`
    - (OAuth consent screen) Set up the App Name, Support Email. The Logo is optional.
    - (Scopes) Add or Remove
    - (Test User) Add your email as a test user to start testing the application.
4. After the consent screen is ready we `can finally create the OAuth client id.`

- Credentials -> Create Credentials -> OAuth client ID.
```
Application Type: Web Application.

Name: FastAPI-Login (or any other name).

Authorized JavaScript origins: http://127.0.0.1:7000.

Authorized redirect URIs: http://127.0.0.1:7000/auth. We are going to create this endpoint in the next step.

(These urls should be modified to allow requests from your domain when the app is hosted in a server.)
```

## Create OAuth client
- We need the `client_id` and `the client_secret`.
- Use the environment variables `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`
```
$ export GOOGLE_CLIENT_ID=...
$ export GOOGLE_CLIENT_SECRET=...
```
- Set secrete key
```
$ export SECRET_KEY=...
```