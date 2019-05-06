# Heimkok-Bot
Just a simple discord-bot for personal use.

To use this, acquire a bot token from discord and an API token from OpenWeatherMap.

Launch the bot: `./heimkok.py`, you will get a little ready message when the bot's ready to go. Make sure the bot and weather API tokens are exported as environment variables named BOT_TOKEN and WEATHER_API_TOKEN.

## To launch as a Docker container:
Create a Dockerfile in the same directory as all the python code with the following content:
```
FROM python:3.6-alpine

COPY . /bot

WORKDIR /bot

RUN pip3 install -U discord.py
RUN pip3 install -U requests

ENV BOT_TOKEN <your_bot_token>
ENV WEATHER_API_TOKEN <your_openweathermap_token>

CMD ["python3", "./heimkok.py"]

```
Build the image:
```
docker build -t heimkok-bot .
```
Launch the container:
```
docker run -d heimkok-bot
```
