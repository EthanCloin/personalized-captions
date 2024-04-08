from dotenv import load_dotenv
import os
import httpx


load_dotenv()
BASIC_DISPLAY_APP_ID = int(os.getenv("BASIC_DISPLAY_APP_ID", -1))
BASIC_DISPLAY_APP_SECRET = os.getenv("BASIC_DISPLAY_APP_SECRET", "")

REDIRECT_URL = "https://www.ethancloin.xyz/"
API_URL = "https://graph.instagram.com"
AUTH_URL = "https://api.instagram.com/oauth/authorize"
TOKEN_URL = "https://api.instagram.com/oauth/access_token"


class Instagram:

    def redirect_to_get_auth_code(self, redirect_url=REDIRECT_URL):
        params = {
            "client_id": BASIC_DISPLAY_APP_ID,
            "redirect_uri": redirect_url,
            "scope": "user_profile,user_media",
            "response_type": "code",
        }
        return httpx.get(AUTH_URL, params=params)

    def swap_auth_code_for_token(self, code: str, redirect_url=REDIRECT_URL):
        body = {
            "client_id": BASIC_DISPLAY_APP_ID,
            "client_secret": BASIC_DISPLAY_APP_SECRET,
            "code": code.split("#_")[0],
            "grant_type": "authorization_code",
            "redirect_uri": redirect_url,
        }

        resp = httpx.post(url=TOKEN_URL, data=body)
        return resp

    def get_my_posts(self, jwt: dict):
        my_posts_url = f"{API_URL}/me/media"
        my_posts_params = {
            "fields": "id,media_type,media_url,caption",
            "access_token": jwt.get("access_token", ""),
        }
        return httpx.get(my_posts_url, params=my_posts_params)
