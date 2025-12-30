# Getting Started

These instructions provide information on usability and accessibility of the program, up and running on your local machine for development and testing purposes.

## System Requirements

The program is made using Python and other downloadable `pip` modules. We recommend installing the version listed below because the program was made on the same version. This increases the stability of the program on the system.

- [Python 3.8.6 (recommended)](https://www.python.org/downloads/release/python-386/)

To use this bot in a server, you need a Discord Account. Discord offers an open API to serve requests for both bots and OAuth2 integrations. Create an application on Discord Developer Portal to access your `TOKEN`.

```bat
cd discord-bot
ren .env_sample .env
```

Rename file `.env_sample` to `.env` and paste your `TOKEN`. Note that the `TOKEN` shown below is fake and is used just for demonstration.

```dotenv
SECRET_TOKEN=SrY2MjR0RET4NTEzMzY5ZTA5.54gQHQ.uxR5Av4peeidM2EXRg_vvTq_Z9I
```

For more information, visit [Discord Documentation](https://discord.com/developers/docs/intro#bots-and-apps).


