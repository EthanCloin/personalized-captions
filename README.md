# goals
- utilize the Instagram API to grab captions and media from the user's profile.
- process those into something we can feed to an OpenAI Assistant
- build an OpenAI Assistant that helps come up with captions for your next post

# dev setup stuff
signup for [ngrok](https://ngrok.com/) and install it on your machine.
this is an HTTPS tunnel to pipe redirects through, hosted on a static domain. 

it's necessary because the Instagram OAuth requires an HTTPS redirect URL. and i am on localhost obv. so i give it the ngrok domain and it pipes the request through to my localhost at the port specified. 

```bash
ngrok http --domain=chicken-deciding-friendly.ngrok-free.app 8080
```

you will need access to the [project dashboard](https://developers.facebook.com/apps/935553515023725/dashboard/) to fill in the values for `.env` variables.
