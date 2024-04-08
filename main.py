from instagram import Instagram
from flask import Flask, request, redirect
from authlib.integrations.flask_client import OAuth
import secrets
import json

app = Flask("Personalized Captions")
app.secret_key = secrets.token_urlsafe(16)

client = Instagram()


@app.route("/")
def hi_world():
    arg = request.args.get("info", "")

    return "hi world: " + arg


@app.route("/login")
def instagram_login():
    resp = client.redirect_to_get_auth_code(
        redirect_url="https://chicken-deciding-friendly.ngrok-free.app/authorize"
    )
    return redirect(resp.url, Response=resp)


@app.route("/authorize")
def instagram_authorize():
    auth_code = request.args.get("code")
    resp = client.swap_auth_code_for_token(
        auth_code,
        redirect_url="https://chicken-deciding-friendly.ngrok-free.app/authorize",
    )
    token = resp.json()

    # TODO: replace w a database op
    with open("ig.jwt", "w") as f:
        json.dump(token, f)
    return redirect("/myposts")


@app.route("/myposts")
def get_my_posts():
    # TODO: replace w a database op
    with open("ig.jwt", "r") as f:
        jwt = json.load(f)

    res = client.get_my_posts(jwt)
    return str(res.json())


def main():
    app.run("0.0.0.0", 8080, debug=True)


if __name__ == "__main__":
    main()
