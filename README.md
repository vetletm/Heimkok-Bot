# Heimkok-Bot
Just a simple discord-bot for personal use.

To use this, acquire a bot token from discord and an API token from OpenWeatherMap.

Launch the bot: `./heimkok.py`, you will get a little ready message when the bot's ready to go. Make sure the bot and weather API tokens are exported as environment variables named BOT_TOKEN and WEATHER_API_TOKEN.

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
