"""Generate secrete key.

- Author: bono
- Email: qhsh9713@gmail.com
"""
import secrets

generated_key = secrets.token_urlsafe(30)
print(generated_key)
