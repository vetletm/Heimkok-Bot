# Heimkok-Bot
Just a simple discord-bot for personal use.

To use this, acquire a bot token from discord and an API token from OpenWeatherMap and a client id and secret from Reddit. The OpenWeatherMap API is to get the weather forecast, and the reddit credentials is used to bleach your eyes.

Launch the bot: `./heimkok.py`, you will get a little ready message when the bot's ready to go. If any environment variables are missing, the bot will raise an exception.

## To launch as a Docker container:
Create a Dockerfile in the same directory as all the python code with the following content:
```
FROM python:3.8-alpine

COPY . /bot

WORKDIR /bot

# Install build-dependencies
RUN apk add --no-cache --virtual .build-deps gcc musl-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Remove unnecessary packages
RUN apk del .build-deps gcc musl-dev

ENV BOT_TOKEN <token>
ENV WEATHER_API_TOKEN <token>
ENV REDDIT_CLIENT_ID <client_id>
ENV REDDIT_CLIENT_SECRET <client_secret>

CMD ["python", "heimkok.py"]


```
With the latest alpine image, the multidict package fails without gcc installed. The above will install it into the image, install the required packages, then uninstalls gcc to save space.

Build the image:
```
docker build -t heimkok-bot .
```
Launch the container:
```
docker run -d heimkok-bot
```

### Dependencies
- Discord.py
- requests
- praw
