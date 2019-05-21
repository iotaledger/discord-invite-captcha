# Discord Invite Generator

This small web application will serve a reCaptcha challange, on success it will generate a one-time use invite for a Discord channel.
The purpose of this is to prevent a flood of bots from joining your Discord server by re-using invites.

## Requirements

To run this bot you need the following packages installed on your system:

 - Python 3.5+

## Installation

 - Install all python package dependancies (in a virtualenv by preference) with `pip install -r requirements.txt`
 - Add your discord keys and other configuration to the `.env` file (see .env.example to see the variable names to use)
 - Run `FLASK_APP=server.py flask run` to start the bot as the active process

## Using Docker

This bot runs using Docker as well, expose port 5000 for this.

```
docker build . -t discord_captcha -f Dockerfile
docker run -p 5000:5000 --network host discord_captcha
```


## Used environment variables in the .env file

 - `SITE_KEY` - reCaptcha v2 site key
 - `SECRET_KEY` - reCaptcha v2 secret key
 - `CHANNEL_ID` - The Channel ID of the Discord Channel you want to invite for
 - `DISCORD_TOKEN` - The Bot token for your Discord bot, this bot needs to have invite permissions for your server.

